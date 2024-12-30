import requests

#-----------------------------------------------------------
#--------------------GET POŽADAVEK--------------------------
#-----------------------------------------------------------
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
code = response.status_code # dostaneme číselný kód odpovědi
msg = response.text # zde se uloží obsah odpovědi jako string
body = response.json() # zde dojde k dekódování odpovědi do pythonovského slovníku # tělo odpovědi si převedu na list uživatelů

#print("Code: ",response.status_code)
#print("Odpověď: ")
# vytisknu si počet údajů/uživatelů/userů
#print(len(body))

#-----------------------------------------------------------
#--------------------POST POŽADAVEK-------------------------
#-----------------------------------------------------------

body1 = {
    "title": "foo",
    "body": "toto je můj nový článek",
    "userId": 1,
}
response1 = requests.post("https://jsonplaceholder.typicode.com/posts/", json=body1)
code1 = response1.status_code
print("POST POŽADAVEK")
print(code1)
print(response1.json())
#CVIČENÍ : Napište kód, který vytvoří uživatele na stránce JSONPlaceholder

body2 = {
    "username": "Engeto",
    "password": "1234",
    "name": "Honza",
    "surname": "Novák",
    "email": "honza.novak@engeto.com",
    "age": 25,
}
response2 = requests.post("https://jsonplaceholder.typicode.com/users/", json=body2)
code2=response2.status_code

print(code2)
print(response2.json())
#-----------------------------------------------------------
#--------------------PUT POŽADAVEK--------------------------
#-----------------------------------------------------------
#Změní údaje
body3 = {
    "email": "sincere@engeto.com",
}
response3 = requests.put("https://jsonplaceholder.typicode.com/users/1", json=body3)
code3 = response3.status_code
print("PUT POŽADAVEK")
print(code3)
print(response3.json())
#Cvičení, změnit body článku id 8
body4={
 "body": "tento článek teď vypadá úplně jinak než předtím",
}
response4 = requests.put("https://jsonplaceholder.typicode.com/users/8", json=body4)
code4=response4.status_code
print("CVIČENÍ PUT")
print(code4)
print(response4.json())

#-----------------------------------------------------------
#--------------------DELETE POŽADAVEK------------------------
#-----------------------------------------------------------
response5 = requests.delete("https://jsonplaceholder.typicode.com/users/9")#Smazání uživatele id 9
print("CVIČENÍ DELETE")
print(response5.status_code)
print(response5.json())
#Cvičení - smazání fotky
response6 = requests.delete("https://jsonplaceholder.typicode.com/photos/50")
print(response6.status_code)
print(response6.json(),response6.text)
#--------------------CVIČENÍ/ÚKOL------------------------
#Všem článkům, jejichž title začíná na písmeno "n" změň parametr body na "tento článek teď vypadá úplně jinak než předtím".
# získám všechny články na webu:
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
# projdu všechny články a pokud najdu článek s title začínající na "n", tak ho upravím:
for post in posts:
    if post["title"][0] == "n":
        new_body = {
            "body": "tento článek teď vypadá úplně jinak než předtím"
        }  # nový obsah článku
        post_id = post["id"]  # id článku
        # PUT požadavek
        response = requests.put(
            f"https://jsonplaceholder.typicode.com/posts/{post_id}", data=new_body
        )
        # vtisknu odpověď
        print(response.status_code)
        print(response.json())

