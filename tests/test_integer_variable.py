"""Tests for the integer_variable module."""

import pytest
from integer_variable import get_integer_variable, set_integer_variable


def test_get_integer_variable_returns_int():
    """Test that get_integer_variable returns an integer."""
    result = get_integer_variable()
    assert isinstance(result, int)


def test_set_integer_variable_updates_value():
    """Test that set_integer_variable updates the value."""
    set_integer_variable(100)
    assert get_integer_variable() == 100


def test_set_integer_variable_with_negative_number():
    """Test setting a negative integer."""
    set_integer_variable(-5)
    assert get_integer_variable() == -5


def test_set_integer_variable_with_zero():
    """Test setting zero."""
    set_integer_variable(0)
    assert get_integer_variable() == 0


def test_set_integer_variable_with_float_raises_type_error():
    """Test that setting a float raises TypeError."""
    with pytest.raises(TypeError):
        set_integer_variable(3.14)


def test_set_integer_variable_with_string_raises_type_error():
    """Test that setting a string raises TypeError."""
    with pytest.raises(TypeError):
        set_integer_variable("42")