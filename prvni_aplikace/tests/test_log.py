import math
import pytest
from src import quadratic_formula

#pro spuštění voláme % pytest prvni_aplikace/tests/test_log.py 
#Test, zda vrací správné výpočty
@pytest.mark.parametrize("a,b,c,expected", 
[(1,2,1,(-1,-1)) ],
)
def test_log(a,b,c,expected):
    assert quadratic_formula.solve_quadratic_formula(a,b,c) == expected