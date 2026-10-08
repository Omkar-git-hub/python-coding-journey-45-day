import pytest
from find_quotient import find_quotient

def test_find_quotient_positive():
    assert find_quotient(10, 2) == 5

def test_find_quotient_negative():
    assert find_quotient(-10, 2) == -5

def test_find_quotient_negative_divisor():
    assert find_quotient(10, -2) == -5

def test_find_quotient_zero_dividend():
    assert find_quotient(0, 5) == 0

def test_find_quotient_zero_divisor():
    with pytest.raises(ValueError):
        find_quotient(10, 0)