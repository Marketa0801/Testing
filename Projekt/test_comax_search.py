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

# Zadání klíčového slova do vyhledávacího pole
    search_field = page.locator("input[id='edit-keys']")
    search_field.fill("plechové krytiny")
# Ověření, že pole obsahuje správné klíčové slovo
    assert search_field.input_value() == "plechové krytiny"

