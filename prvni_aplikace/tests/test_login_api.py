import pytest
from src import login_api
users = {
    "admin": ["admin", "tajemství", "authTokenAdmina"],
    "joe": ["heslo", "tajemství_joa", "authTokenJoa"],
    "fred": ["password", "tajemství_freda", "authTokenFreda"],
    "bob": ["1234", "tajemství_boba", "authTokenBoba"],
}
#pro spuštění voláme % pytest prvni_aplikace/tests/test_login_api.py

#Otestovat funkčnost. Zda při zadání správných hodnot vrací správné informace - tzv."Tajemství"
#Otestování přihlášení se správnými údaji a získání authToken
#Otestování výjimek
#Otestovat Neexistujícího uživatele "LookupError"
#Otestovat Nesprávné heslo "NameError"
#Otestovat Neexistujícho uživatele s existujícím tokenem
#Otestovat odhlášení existujícho uživatele. 

#Úspěšné Přihlášení (správný user i password)
@pytest.mark.parametrize("username, password, expected_authToken",
[   ("admin","admin","authTokenAdmina"),
    ("joe","heslo","authTokenJoa"),
    ("fred","password","authTokenFreda"),
    ("bob","1234","authTokenBoba")
],
)
def test_login(username, password, expected_authToken):
    assert login_api.login(username,password) == expected_authToken
    login_api.logout(expected_authToken)

#Neúspěšná přihlášení (správný user a špatné password a zároveň neexistující user a heslo)
@pytest.mark.parametrize("username,password,expected_exception,expected_msg",
[   ("admin","admirál",NameError,"Neplatné heslo"),
    ("joe","spatne_heslo",NameError,"Neplatné heslo"),
    ("frantisek","password",LookupError,"Neplatné jméno nebo heslo"),
    ("bohouš","1234",LookupError,"Neplatné jméno nebo heslo")
 ],
)
def test_invalid_password(username,password,expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        login_api.login(username,password)


#Otestování získání tajemství
@pytest.mark.parametrize("user,pssw,expected_secret", 
[   ("admin","admin","tajemství"),
    ("joe","heslo","tajemství_joa"),
    ("fred","password","tajemství_freda"),
    ("bob","1234","tajemství_boba")
],
)
def test_get_secret(user,pssw,expected_secret):
    token = login_api.login(user,pssw)
    assert login_api.get_secret == expected_secret
    login_api.logout(token)
def test_get_secret_wrong_auth():
    with pytest.raises(ValueError):
        login_api.get_secret("random")

#Otestování odhlášení
@pytest.mark.parametrize(
    "user, passwd",
    [("admin", "admin"), ("joe", "heslo"), ("bob", "1234"), ("fred", "password")],
)
def test_logout(user, passwd):
    token = login_api.login(user, passwd)
    login_api.logout(token)
    with pytest.raises(ValueError):
        login_api.get_secret(token)