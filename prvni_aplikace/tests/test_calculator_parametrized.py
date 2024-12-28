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

#Test odčítání
@pytest.mark.parametrize("c,d,vysledek",
[(1,2,-1),
 (0,2,-2),
 (0,0,0),
 (-5,-2,-3)
 ],  )
def test_subtract(c,d,vysledek):
    assert calculator.subtract(c,d) == vysledek

#Test násobení
@pytest.mark.parametrize("e,f,ocekavany_vysledek",
[(2,3,6),
 (-2,3,-6),
 (4,-2,-8),
 (0,0,0)],                )
def test_multiply(e,f,ocekavany_vysledek):
    assert calculator.multiply(e,f) == ocekavany_vysledek

@pytest.mark.parametrize("g,h,result_expected",
[(2,3,6),
 (-2,3,-6),
 (4,-2,-8),
 (0,0,0)],)
def test_multiply_wrong(g,h,result_expected):
    assert calculator.multiply_wrong(g,h) == result_expected