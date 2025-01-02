#------------------TEST TLAČÍTKA---------------
#Testuje, zda hlavní tlačítko na domovské stránce správně přesměruje.
import pytest
#pro spuštění voláme % pytest Projekt/test_comax.py

def test_kontakty(page):
#Vstup na stránku
        page.goto("https://www.strechycomax.cz/")  

#Zpracování cookies, pokud se objeví. 
        try:
            cookies_button = page.locator("text=Souhlasím").first 
            if cookies_button.is_visible():
                cookies_button.click()
        except:
            pass
# Kliknutí na odkaz "Kontakty"
    page.locator("a:has-text('Kontakty')").click()

# Ověření, přesměrování
    assert page.url == "https://www.strechycomax.cz/kontakt"