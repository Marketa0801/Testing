#------------------TEST FORMULÁŘE---------------
#Testuje, zda formulář Poptávka lze správně vyplnit
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

#Otevření prohlížeče
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, slow_mo=1000
        )
        yield browser
        

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
  
 
def test_formulare(page: Page):
#Vstup na stránku
    page.goto("https://www.strechycomax.cz/poptavka") 
#Cookies
    refuse_button = page.locator("div.ch2-dialog-actions button.ch2-deny-all-btn", has_text="Jen nezbytné")
    refuse_button.click()
# Viditelnost formuláře
    form_locator = page.locator("#webform-submission-poptavka-paragraph-456-add-form") 
    assert form_locator.is_visible(), 

# Ověření existence polí ve formuláři
    fields = [
        "input[name='jmeno_a_prijmeni']",
        "input[name='e_mail']",
        "input[name='telefonni_cislo']",
        "select[name='kraj_realizace']", 
        "select[name='mam_zajem_o']",
        "select[name='doplnkove_sluzby[]']",
        "textarea[name='zprava']"
      ]
    for field in fields:
        assert page.locator(field).is_visible(), f"Pole {field} není viditelné"


    

