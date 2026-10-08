"""Tests for print_multiple_variables module."""

import io
from contextlib import redirect_stdout

from print_multiple_variables import print_multiple_variables


def test_print_multiple_variables():
    """Test that print_multiple_variables prints the expected output."""
    output = io.StringIO()
    with redirect_stdout(output):
        print_multiple_variables()
    assert output.getvalue() == "Name: Alice, Age: 30, City: New York\n"