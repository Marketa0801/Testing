#------------------TEST VYHLEDÁVÁNÍ---------------
#Testuje funkčnost vyhledávání při použití mobilního telefonu. 
#Zda po vložení klíčového slova do vyhledávacího pole zobrazí výsledky s daným slovem. 
import pytest
from playwright.sync_api import sync_playwright

#Otevření a zavření prohlížeče
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, slow_mo=1000
        )
        yield browser
        browser.close()
#Oteření a zavření okna
@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_search(page):
#Zmenšení velikosti obrazovky prohlížeče na velikost obrazovky mobilního telefonu
    page.set_viewport_size({"width": 375, "height": 667})  

#Vstup na stránku
    page.goto("https://www.strechycomax.cz/") 
#Odmítnutí cookies
    refuse_button = page.locator("div.ch2-dialog-actions button.ch2-deny-all-btn", has_text="Jen nezbytné")
    refuse_button.click()
 
# Kliknutí na tlačítko pro otevření mobilního menu
    mobile_menu_button = page.locator("#mobile-menu-button")
    mobile_menu_button.click()  

#Kliknutí na "lupičku"
    magnifer_button = page.locator("#block-comax-vyhledavani")
    magnifer_button.click()

#Nalezení vyhledávacího pole
    search_field = page.locator("input[id='edit-keys']")
#Ověření, že vyhledávací pole existuje a bylo nalezeno
    assert search_field.is_visible()

#Zadání klíčového slova do vyhledávacího pole
    search_field.fill("plechové krytiny")
#Ověření, že pole obsahuje správné klíčové slovo
    assert search_field.input_value() == "plechové krytiny"

#Lokalizace tlačítka pro odeslání vyhledávání
    button_locator = page.locator("input[type='submit'][id='edit-submit']")
    button_locator.wait_for(state="visible",timeout=10000)
# Kliknutí na tlačítko vyhledávání
    button_locator.click()
# Čekání na načtení stránky 
    page.wait_for_load_state("load")

# Čekání na načtení výsledků vyhledávání
    results_locator = page.locator("div.item-list")  # Přizpůsobte podle skutečného selektoru
    results_locator.wait_for(state="visible", timeout=10000)

# Ověření, že výsledky obsahují klíčové slovo "plechové krytiny"
    result_items = page.locator("ol.search-results")  
    assert result_items.count() > 0  

# Ověření pro každý výsledek, že obsahuje klíčové slovo
    for item in result_items.all():  
        item_text = item.text_content()
        assert "plechové krytiny" in item_text.lower()  




