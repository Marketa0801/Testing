#------------------TEST ODKAZU---------------
#Testuje, zda tlačítko Kontakty z hlavního menu na domovské stránce správně přesměruje.
import pytest

def test_kontakty(page):
#Vstup na stránku
    page.goto("https://www.strechycomax.cz/")  
#Cookies není třeba odklikávat jelikož je web řeší speciálním odkazem v zápatí stránky. 

# Čekám na prvek, aby byl viditelný a interaktivní
    contact_link = page.locator("#block-comax-main-menu .menu-item a[href='https://www.strechycomax.cz/kontakt']") # Bylo nutné velmi specifikovat lokátor, jelikož na stránce se text="Kontakt" jich nachází mnoho. 
    contact_link.wait_for(state="visible", timeout=10000)  
    
# Kliknutí na prvek
    contact_link.click()

# Ověření přesměrování
    page.wait_for_url("https://www.strechycomax.cz/kontakt", timeout=10000)  
    assert page.url == "https://www.strechycomax.cz/kontakt" 
