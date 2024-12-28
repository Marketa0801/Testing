#TESTOVÁNÍ VÍCE PARAMETRŮ
#pro spuštění voláme pytest tests/test_calculator_parametrized.py
import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5,-8) == -3