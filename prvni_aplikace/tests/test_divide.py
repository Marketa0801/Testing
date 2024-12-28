import pytest
from src import calculator
#Otestování dělení a chybové hlášky
#pro spuštění voláme % pytest prvni_aplikace/tests/test_divide.py

#Test, ktery neni vyhodnocen spravně - naivní varianta
#def test_divide_naive():
#   assert calculator.divide(5,0) == ValueError

#Test jiz zohlednuje vyjimku
def test_divide():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

#Otestování zprávy u vyjímky
def test_divide():
    with pytest.raises(ValueError) as exc: #Ukládá informace o vyvolané chybě do proměnné exc
        calculator.divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!" #Ověřuje, že text zprávy(v proměnné, která je ve stringu) odpovídá očekávanému textu

#Parametrizované výjimky
import math #Import funkce

def log(a, b):
    if a <= 0:
        raise ValueError("Cannot take log of non-positive number!")
    if b <= 0:
        raise ZeroDivisionError("Cannot take log with non-positive base!")
    if b == 1:
        raise NameError("Cannot take log with base 1!")
    return math.log(a, b)
#Vytvoření testu s různými typy výjimek
@pytest.mark.parametrize(
    "a, b, expected_exception, expected_msg",
    [
        (0, 5, ValueError, "Cannot take log of non-positive number!"),
        (-2, 5, ValueError, "Cannot take log of non-positive number!"),
        (9, -2, ZeroDivisionError, "Cannot take log with non-positive base!"),
        (5, 1, NameError, "Cannot take log with base 1!"),
    ],
)
def test_log(a, b, expected_exception, expected_msg):
    with pytest.raises(expected_exception) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_msg