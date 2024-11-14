import math

import pytest
from SLAE import Gauss
from integration import integr_Simpson
from NotLinearEquation import newton

def test_Gauss():
    assert Gauss(
        [[3,4,6,6],
        [2,3,8,1],
        [5,4,2,6]]) == [-2.333, 5.0, -1.167]

def test_integr_Simpson():
    assert integr_Simpson(math.log(2,math.e)) == 0.5

def test_newton():
    assert newton(4,5) == 4.47