#------------------TEST ODKAZU---------------
#Testuje, zda tlačítko Kontakty z hlavního menu na domovské stránce správně přesměruje.
import pytest
from playwright.sync_api import sync_playwright

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

def test_kontakty(page):


    #Vstup na stránku
    page.goto("https://www.strechycomax.cz/") 
    #Cookies
    refuse_button = page.locator("div.ch2-dialog-actions button.ch2-deny-all-btn", has_text="Jen nezbytné")
    refuse_button.click()

# Čekám na prvek, aby byl viditelný a interaktivní
    contact_link = page.locator("#block-comax-main-menu .menu-item a[href='https://www.strechycomax.cz/kontakt']") # Bylo nutné velmi specifikovat lokátor, jelikož na stránce se text="Kontakt" jich nachází mnoho. 
    contact_link.wait_for(state="visible", timeout=10000)  
    
# Kliknutí na prvek
    contact_link.click()

# Ověření přesměrování
    page.wait_for_url("https://www.strechycomax.cz/kontakt", timeout=10000)  
    assert page.url == "https://www.strechycomax.cz/kontakt" 
