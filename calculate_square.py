"""
calculate_square.py

Provides a simple function to calculate the square of a number.

The function accepts an integer or a float and returns the square of the
input.  It relies on Python's built-in multiplication, so it will raise a
TypeError if the input is not a numeric type.

Examples
--------
>>> calculate_square(5)
25
>>> calculate_square(3.5)
12.25
>>> calculate_square(-4)
16
"""

from __future__ import annotations

__all__ = ["calculate_square"]


def calculate_square(number: int | float) -> int | float:
    """
    Return the square of *number*.

    Parameters
    ----------
    number : int | float
        The number to square.

    Returns
    -------
    int | float