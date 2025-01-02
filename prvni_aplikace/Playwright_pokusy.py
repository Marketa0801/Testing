# modul pro práci s operačním systémem
import os    
# modul pro přístup k některým systémovým proměnným 
import sys 
# modul pro práci s pseudo-náhodnými procesy    
import random  

import math

print(
    "os" in dir() \
    and "sys" in dir() \
    and "random" in dir()
)
print("muj_modul" in dir())

print(help(os))

#----------------LOKÁTORY---------------------
#objekt = page.locator('cesta_v_lokátoru')
#objekt = page.locator('cesta_do_divu_1').locator("cesta_v_divu_1_do_jeho_potomka")
#objekt.click()
#Textové lokátory
#nadpis = page.locator('text="Toto je text kontejneru"')
#CSS lokátory
#nadpis = page.locator('css=h1')
#nadpis = page.locator('h1')
#Lokátor HTML objektu
#nadpis = page.locator('h1') # všechny objekty typu `h1` na stránce
#Lokátor třídy
#div_1 = page.locator('.container') # všechny objekty se třídou ".container", bez uvozovek
#Lokátor třídy a HTML objektu
#div_2 = page.locator("div.container_2") # všechny divy se třídou "container_2" (pokud by na stránce byl třeba <p> s touto třídou, tak ho lokátor nenajde)
         #jde to po sobě: název HTML objektu, tečka, název třídy, bez mezer, uvozovek apod.
#Lokátor ID
#inp_password = page.locator("#password") # všechny objekty s id "password" / tečka vyměníme za #
#Lokátor ID a HTML objektu
#div_2 = page.locator("input#password") # všechny inputy s id "password"
#Ostatní lokátory
#inp_password = page.locator("input[type='password']") # všechny inputy s atributem type s hodnotou password
#h1_2 = page.locator(".container_2 > h1") # všechny h1, které jsou přímé děti objektu se třídou ".container_2"
#h1_2 = page.locator("body > h1") # všechny h1, které jsou přímé děti objektu body
#h1_2 = page.locator(".container >> .nadpis") # všechny třídy "nadpis", které se nacházejí v nějakém objektu se třídou ".container"



#nadpis = page.locator ('text="Nadpis2"')
#nadpis2 = page.locator('.container-2')
#nadpis3 = page.locator('name="head"')
#nadpis4 = page.locator("h1#heading")

#----------------FUNKČNÍ LOKÁTORY---------------------
#Lokátor :HAS-TEXT()
#div_1 = page.locator(":has-text('Nad')") #Vybírá všechny objekty, v nichž se někde nachází text, jehož součástí je string, který dostal jako parametr.
#div_1 = page.locator("div:has-text('Nad')") #Kombinace s HTML lokátorem
#Lokátor :HAS()
#div = page.locator("div:has(h1)")
#Lokátor nth()
#div_1 = page.locator(":nth-match(div, 0)") # ze všech divů na stránce vybere první
#div_1 = page.locator("div").nth(0) # ze všech divů na stránce vybere první


#-----------------XPATH LOKÁTORY--------------------------
#header = page.locator("//div[@id='header']")  #můžete používat s prefixem "xpath=", nebo bez něj.
