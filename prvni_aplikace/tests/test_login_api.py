import pytest
from src import login_api
#pro spuštění voláme % pytest prvni_aplikace/tests/test_login_api.py

#Otestovat funkčnost. Zda při zadání správných hodnot vrací správné informace - tzv."Tajemství"
#Otestování přihlášení se správnými údaji a získání authToken
#Otestování výjimek
#Otestovat Neexistujícího uživatele "LookupError"
#Otestovat Nesprávné heslo "NameError"
#Otestovat Neexistujícho uživatele s existujícím tokenem
#Otestovat odhlášení existujícho uživatele. 

#Úspěšné Přihlášení
@pytest.mark.parametrize("username, password, authToken",
[("admin","admin","authTokenAdmina"),
 ("joe","heslo","authTokenJoa"),
 ("fred","password","authTokenFreda"),
 ("bob","1234","authTokenBoba")],
)
def test_login(username, password, authToken):
    assert login_api.login(username,password) == authToken

#Neúspěšná přihlášení (špatné heslo)
@pytest.mark.parametrize("username,password,expected_exception,expected_msg",
[("admin","admirál",NameError,"Neplatné heslo"),
 ("joe","spatne_heslo",NameError,"Neplatné heslo"),
 ("fred","heslo",NameError,"Neplatné heslo"),
 ("bob","heslo",NameError,"Neplatné heslo") ],
)
def test_invalid_password(username,password,expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        login_api.login(username,password)
    assert str(exc.value) == expected_msg

#Neúspěšná přihlášení (špatné uživatelské jméno)
@pytest.mark.parametrize("username,password,expected_exception,expected_msg",
[("administrator","admin",LookupError,"Neplatné jméno nebo heslo"),
 ("josef","heslo",LookupError,"Neplatné jméno nebo heslo"),
 ("frantisek","password",LookupError,"Neplatné jméno nebo heslo"),
 ("bohouš","1234",LookupError,"Neplatné jméno nebo heslo"),]
)
def test_invalid_password(username,password,expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        login_api.login(username,password)
    assert str(exc.value) == expected_msg