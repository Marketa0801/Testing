import pytest # import knihovny pytest
from src import calculator #import testovaného souboru

#První test - sčítání
def test_add():
    assert calculator.add(5,3) == 8 #volání funkce add ze souboru calculator
#Selhávající test - sčítání
def test_add_2():
    assert calculator.add_wrong(5,3) == 8
#Test -  Odčítání
def test_subtract():
    assert calculator.subtract(5,3) == 2
    assert calculator.subtract(-1,5) == -6
#Test  - násobení
def test_multiply():
    assert calculator.multiply(5,3) == 15
#Selhávající test - násobení
def test_multyply2():
    assert calculator.multiply_wrong(5,3) == 15
#Test - dělení
def test_divide():
    assert calculator.divide(10,2) == 5
    assert calculator.divide(-6,2) == -3