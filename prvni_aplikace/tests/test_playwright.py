import pytest
#pro spuštění voláme % pytest prvni_aplikace/tests/test_playwright.py
def test_title(page):
    page.goto("https://www.google.com/")
    title = page.locator("title")
    assert title.inner_text() == "Google"

#-----------COOKIES---------------------
#estujeme, jestli poté, co odmítneme souhlas se zpracováváním cookies, celá cookies lišta zmizí.
def test_click_cookies(page):   #Definice funkce
    id_cookie_bar = "CXQnmb"   #ID tlačítka na odmítnutí a ID celé lišty - našli jsme prozkoumáváním stránky (např. pomocí Inspectora)
    id_button_refuse = "W0wltc"

    page.goto("https://www.google.com/") #Přechod na testovanou stránku
    refuse_button = page.locator(f"button#{id_button_refuse}")  #Lokátor tlačítka na které chceme kliknout
    refuse_button.click()                   #Klik

    cookie_bar = page.locator(f"div#{id_cookie_bar}")   #Lokátor celé lišty
    assert cookie_bar.is_visible() == False   #testujeme, že cookies lišta není vidět


#Jen odmítnutí cookies
def test_click_cookies(page):
    id_button_refuse = "W0wltc"

    page.goto("https://www.google.com/")
    refuse_button = page.locator(f"button#{id_button_refuse}")
    refuse_button.click()
#CLICK()
#tap() - simuluje kliknutí na mobilu
#dblclick() - simuluje tzv. double-click neboli dvojité kliknutí na element
def test_click(page):
    page.goto("http://www.uitestingplayground.com/click")
    button = page.locator("#badButton")
    button.click()

    button_success = page.locator(".btn-success")
    assert button_success.is_visible() == True
#FILL()
def test_text_input(page):
    page.goto("http://www.uitestingplayground.com/textinput")

    text_input = page.locator("#newButtonName")
    text_input.fill("Hello World")  # do inputu doplníme text "Hello World"

    button = page.locator("#updatingButton")
    button.click() #klikne na tlačítko

    assert button.inner_text() == "Hello World"
#PRESS()
def test_press_enter(page):
    page.goto("http://www.uitestingplayground.com/textinput")

    text_input = page.locator("#newButtonName")
    text_input.fill("Hello World")

    button = page.locator("#updatingButton")
    button.press("Enter")  # stiskni klávesu "Enter"

    assert button.inner_text() == "Hello World"
#HOVER()
#Tato metoda simuluje najetí myši na nějaký objekt.
def test_hover(page):
    page.goto("http://www.uitestingplayground.com/mouseover")
    link = page.locator("text=Click me")
    link.hover()  # simuluje najetí myši na objekt

    alert = page.locator("[title='Active Link']")
    assert alert.is_visible() == True
#ALL()
    #Tento lokátor vybere všechny nadpisy h4 na stránce a my z nich pomocí metody all() uděláme list jednotlivých lokátorů, 
    # které už ukazují na jednotlivé objekty na stránce. Díky tomu pak můžeme přistupovat k něčemu jako je jejich vnitřní text.
def test_more_h4(page):
    page.goto("http://www.uitestingplayground.com/textinput")
    h4 = page.locator("h4")
    h4_list = h4.all()
    assert h4_list[0].inner_text() == "Scenario"
    assert h4_list[1].inner_text() == "Playground"
#DRAG_TO()
#simuluje „přetažení“ objektu z jednoho místa na druhý.
def test_drag_and_drop(page):
    page.goto("https://seleniumbase.io/other/drag_and_drop")

    img = page.locator("#drag1")
    target = page.locator("#div1")

    img.drag_to(target)

    img_new = page.locator("#div1 > img")
    assert img_new.is_visible() == True

#Nahrávání testů
def test_trace(page):
    # Začne nahrávat před začátkem testu
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Jednotlivé kroky testu
    page.goto("http://www.uitestingplayground.com/textinput")

    text_input = page.locator("#newButtonName")
    text_input.fill("Hello World")

    button = page.locator("#updatingButton")
    button.hover()

    # vypne nahrávání po skončení testu a uloží výsledky do souboru trace.zip
    page.context.tracing.stop(path="trace.zip")

