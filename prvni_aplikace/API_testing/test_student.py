import requests
import pytest
#pro spuštění voláme % pytest prvni_aplikace/API_testing/test_student.py
#Příprava dat

URL = "http://108.143.193.45:8080/api/v1/students/"

#Funkce na vytvoření studenta
def create_student(firstName, lastName, email, age):
    body = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "age": age,
    }
    response = requests.post(URL, json=body)
    return response.json()
#Funkce na zjištění existence studenta
def is_student_in_database(id):
    response = requests.get(f"{URL}{id}")
    if response.status_code == 200:
        return True
    else:
        return False
#Funkce na smazání studenta
def delete_student(id):
    response = requests.get(f"{URL}{id}")
    return response.text

#-----------------------------------------------------------
#--------------------TESTOVÁNÍ GET--------------------------
#-----------------------------------------------------------
#Testování na existujícího studenta, kterého jsme si vytvořili
@pytest.mark.parametrize(
    "name, lastname, email, age",
    [
        ("Pepa", "NOVÁK", "pepa.novak@seznam.cz", 25),
        ("Jana", "KOVÁŘOVÁ", "jana.kovarova@seznam.cz", 30),
    ],
)
def test_get_correct_input(name, lastname, email, age):
    student = create_student(name, lastname, email, age) # vytvoříme studenta
    response = requests.get(f"{URL}{student['id']}") # vytvoříme na něj GET požadavek
    delete_student(student["id"]) # studenta smažeme, aby nezůstal v databázi (musíme to udělat ještě před porovnáním, protože to může selhat)
    assert response.status_code == 200 # porovnáme návratový kód
   # zkontrolujeme, že nám byl vrácen správný student:
    assert student["firstName"] == name 
    assert student["lastName"] == lastname
    assert student["email"] == email
    assert student["age"] == age

#Testování na neexistujícího studenta - například s id 5000
@pytest.mark.parametrize("id", 
    [(5000)]
)
def test_get_incorrect_input(id):
     #Zjištění pomocí fumkce zda student existuje
    response2 = requests.get(f"{URL}{id}")
    assert response2.status_code == 401
    assert response2.text == "Student not found"

#-----------------------------------------------------------
#--------------------TESTOVÁNÍ DELETE-----------------------
#-----------------------------------------------------------
#Smazání existujícího studenta
@pytest.mark.parametrize(
    "name, lastname, email, age",
    [
        ("Pepa", "NOVÁK", "pepa.novak@seznam.cz", 25),
        ("Jana", "KOVÁŘOVÁ", "jana.kovarova@seznam.cz", 30),
    ],
)
def test_delete_correct_input(name, lastname, email, age):
    student = create_student(name, lastname, email, age) #Vytvoření studenta, ať mám co mazat
    response = requests.delete(f"{URL}{student['id']}") #Vytvoření požadavku na smazání
    assert response.status_code == 200 # Kontrola, zda je odpověď OK 200 - spíše by to ale mělo být 204
    assert is_student_in_database(student["id"]) == False # zjistíme, zda byl student opravdu smazán

#Mazání neexistujícího studenta
#Abych nemazala nějaká data, která existují, pro účely testu si studenta vytvořím, smažu a pak pošlu požadavek na smazání neexistujícího

def test_delete_incorrect_input():
    student = create_student("Pepa", "NOVÁK", "něco@něco.cz", 25) # vytvořím studenta
    delete_student(student["id"]) # smažu studenta
    response = requests.delete(f"{URL}{student['id']}") # studenta se pokusím smazat přes enpoint
    code = response.status_code

    # operace // je celočíselné dělení - např. 5 // 2 = 2, 4 // 2 = 2, 8//5 = 1
    # pokud dělíme 3ciferné číslo 100, dostaneme jeho první číslici
    first_digit = code // 100 
    assert first_digit != 2 #testovat pouze podmínku, že status kód nezačíná číslicí 2 (tedy, že nám dá najevo, že se něco nepovedlo).

#Otestování záporného ID
@pytest.mark.parametrize(
    "id",
    [-1, -152, -988001],
)
def test_delete_negative_id(id):
    response = requests.delete(f"{URL}{id}")
    assert response.status_code == 500

#-----------------------------------------------------------
#--------------------TESTOVÁNÍ POST-----------------------
#-----------------------------------------------------------
def test_post(name, lastname, email, age, expected_code):
    response = requests.post(
        URL, json={"firstName": name, "lastName": lastname, "email": email, "age": age}
    )
    code = response.status_code
    body = response.text

    # pokud je odpověď serveru 2xx, tak se student v databázi pravděpodobně vytvořil → musíme ho po sobě smazat
    # zároveň se v body nachází odpověď, kterou lze převést na json a získat informace vytvořeného studenta
    if code // 100 == 2:
        body = response.json()
        delete_student(body["id"])

    # zjišťujeme, jestli odpověď serveru odpovídá očekávanému kódu
    assert code == expected_code

    # pokud jsme očekávali odpověď serveru 2xx, tak chceme zkontrolovat i tělo odpovědi
    if expected_code // 100 == 2:
        assert body["firstName"] == name
        assert body["lastName"] == lastname.upper()
        assert body["email"] == email
        assert body["age"] == age