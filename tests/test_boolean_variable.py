"""Tests for the boolean_variable module."""

import boolean_variable


def test_boolean_variable_is_true():
    """Test that boolean_variable is True."""
    assert boolean_variable.boolean_variable is True


def test_boolean_variable_is_bool():
    """Test that boolean_variable is of type bool."""
    assert isinstance(boolean_variable.boolean_variable, bool)