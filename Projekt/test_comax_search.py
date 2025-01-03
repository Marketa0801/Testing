#------------------TEST VYHLEDÁVÁNÍ---------------
#Testuje funkčnost vyhledávání. Zda po vložení klíčového slova do vyhledávacího pole zobrazí výsledky s daným slovem. 
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
#Vstup na stránku
    page.goto("https://www.strechycomax.cz/") 
#Odmítnutí cookies
    refuse_button = page.locator("div.ch2-dialog-actions button.ch2-deny-all-btn", has_text="Jen nezbytné")
    refuse_button.click()
#Nalezení vyhledávacího pole
    search_field = page.locator("input[id='edit-keys']")
#Ověření, že vyhledávací pole existuje a bylo nalezeno
    assert search_field.is_visible()

#Zadání klíčového slova do vyhledávacího pole
    
    search_field.fill("plechové krytiny")
#Ověření, že pole obsahuje správné klíčové slovo
    assert search_field.input_value() == "plechové krytiny"
# Skrýt překážející prvek
    page.evaluate("document.querySelector('.search-switcher').style.display = 'none'")

#Lokalizace tlačítka pro odeslání vyhledávání
    button_locator = page.locator("input[id='edit-submit']")
    button_locator.wait_for(state="visible")
# Kliknutí na tlačítko vyhledávání
    button_locator.click()
# Čekání na načtení stránky 

    page.wait_for_load_state("load")

# Debug: Po kliknutí na tlačítko udělat screenshot
    page.screenshot(path="Projekt/after_search_click.png")


