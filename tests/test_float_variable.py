import pytest

from float_variable import float_variable

def test_float_variable_exists():
    """The float_variable should be defined."""
    assert float_variable is not None

def test_float_variable_type():
    """The float_variable should be of type float."""
    assert isinstance(float_variable, float)

def test_float_variable_value():
    """The float_variable should have the expected value."""
    assert float_variable == 3.14159