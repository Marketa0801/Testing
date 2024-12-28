#TESTOVÁNÍ VÍCE PARAMETRŮ
#pro spuštění voláme % pytest prvni_aplikace/tests/test_calculator_parametrized.py 
import pytest
from src import calculator

#Test sčítání s více parametry
def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5,-8) == -3
#Selhávající test sčítání s více parametry
def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0,0) == 0

#Test sčítání s více parametry pomocí @pytest.mark.parametrize 
@pytest.mark.parametrize("a,b,expected",
 [(1,2,3),
  (0,2,2),
  (-2,9,7),
  (5,-8,-3)
   ],   )
def test_add_parametrize(a,b,expected):
   assert calculator.add(a,b) == expected

#Selhávající Test sčítání s více parametry pomocí @pytest.mark.parametrize 
@pytest.mark.parametrize("x,y,expected_result",
[ (1,2,3),
  (0,2,2),
  (-2,9,7),
  (0,0,0) ],   )
def test_add_wrong_parametrize(x,y,expected_result):
    assert calculator.add_wrong(x,y) == expected_result