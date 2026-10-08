"""
Tests for the string_to_integer module.
"""

import pytest
from string_to_integer import convert_string_to_integer, safe_convert_string_to_integer


class TestConvertStringToInteger:
    """Tests for convert_string_to_integer function."""

    def test_convert_positive_integer(self):
        """Test converting a positive integer string."""
        assert convert_string_to_integer("42") == 42

    def test_convert_negative_integer(self):
        """Test converting a negative integer string."""
        assert convert_string_to_integer("-42") == -42

    def test_convert_zero(self):
        """Test converting zero string."""
        assert convert_string_to_integer("0") == 0

    def test_convert_large_number(self):
        """Test converting a large number string."""
        assert convert_string_to_integer("123456789") == 123456789

    def test_convert_with_leading_zeros(self):
        """Test converting a string with leading zeros."""
        assert convert_string_to_integer("007") == 7

    def test_convert_with_plus_sign(self):
        """Test converting a string with plus sign."""
        assert convert_string_to_integer("+42") == 42

    def test_convert_invalid_string_raises_value_error(self):
        """Test that invalid string raises ValueError."""
        with pytest.raises(ValueError):
            convert_string_to_integer("not_a_number")

    def test_convert_empty_string_raises_value_error(self):
        """Test that empty string raises ValueError."""
        with pytest.raises(ValueError):
            convert_string_to_integer("")

    def test_convert_float_string_raises_value_error(self):
        """Test that float string raises ValueError."""
        with pytest.raises(ValueError):
            convert_string_to_integer("3.14")


class TestSafeConvertStringToInteger:
    """Tests for safe_convert_string_to_integer function."""

    def test_safe_convert_valid_integer(self):
        """Test safe conversion of valid integer string."""
        assert safe_convert_string_to_integer("42") == 42

    def test_safe_convert_negative_integer(self):
        """Test safe conversion of negative integer string."""
        assert safe_convert_string_to_integer("-42") == -42

    def test_safe_convert_zero(self):
        """Test safe conversion of zero string."""
        assert safe_convert_string_to_integer("0") == 0

    def test_safe_convert_invalid_string_returns_default(self):
        """Test that invalid string returns default value."""
        assert safe_convert_string_to_integer("not_a_number") == 0

    def test_safe_convert_empty_string_returns_default(self):
        """Test that empty string returns default value."""
        assert safe_convert_string_to_integer("") == 0

    def test_safe_convert_with_custom_default(self):
        """Test safe conversion with custom default value."""
        assert safe_convert_string_to_integer("invalid", default=-1) == -1

    def test_safe_convert_none_returns_default(self):
        """Test that None input returns default value."""
        assert safe_convert_string_to_integer(None) == 0

    def test_safe_convert_float_string_returns_default(self):
        """Test that float string returns default value."""
        assert safe_convert_string_to_integer("3.14") == 0