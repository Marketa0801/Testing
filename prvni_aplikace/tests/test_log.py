import math
import pytest
from src import quadratic_formula

#pro spuštění voláme % pytest prvni_aplikace/tests/test_log.py 
#Test, zda vrací správné výpočty s korektními vstupy
@pytest.mark.parametrize("a,b,c,expected", 
[(1,2,1,(-1,-1)),
 (2,3,-2,(0.5,-2)),
 (1,6,8,(-2,-4)),
 (2,2,0,(0,-1))
   ],
)
def test_log(a,b,c,expected):
    assert quadratic_formula.solve_quadratic_formula(a,b,c) == expected
#Otestování vyjímek
@pytest.mark.parametrize(
 "a, b, c, expected_exception, expected_msg", 
[
    #Koeficient a,b,c musí být ve formátu float nebo int
    ("g",2,1,TypeError,"All coefficients must be of type float or int!"),
    (1,"h",1,TypeError,"All coefficients must be of type