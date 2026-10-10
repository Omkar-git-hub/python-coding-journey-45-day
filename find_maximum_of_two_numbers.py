"""
Find Maximum of Two Numbers

This module provides a single function `find_maximum_of_two_numbers` that
returns the larger of two numeric values.  The function accepts any
objects that support the comparison operators `<` and `>`.  In the
event that the two values are equal, the function simply returns the
first argument.

The implementation is intentionally straightforward to keep the
behaviour consistent with the rest of the repository's simple
utility functions.
"""

def find_maximum_of_two_numbers(a, b):
    """
    Return the maximum of two numbers.

    Parameters
    ----------
    a : int | float | any comparable type
        First value to compare.
    b : int | float | any comparable type
        Second value to compare.

    Returns
    -------
    int | float | any comparable type
        The larger of `a` and `b`.  If both are equal, `a` is returned.

    Examples
    --------
    >>> find_maximum_of_two_numbers(3, 5)
    5
    >>> find_maximum_of_two_numbers(10, 10)
    10
    >>> find_maximum_of_two_numbers(-2, -5)
    -2
    """
    return a if a >= b else b