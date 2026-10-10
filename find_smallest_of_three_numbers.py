"""
Utility to find the smallest of three numbers.

This module provides a single function, :func:`find_smallest_of_three_numbers`,
which accepts three numeric arguments and returns the smallest among them.
The implementation follows the same style as the existing
``find_largest_of_three_numbers`` helper in the repository.
"""

def find_smallest_of_three_numbers(a, b, c):
    """
    Return the smallest of three numbers.

    Parameters
    ----------
    a : int | float
        First number.
    b : int | float
        Second number.
    c : int | float
        Third number.

    Returns
    -------
    int | float
        The smallest of the three input values.

    Examples
    --------
    >>> find_smallest_of_three_numbers(3, 1, 2)
    1
    >>> find_smallest_of_three_numbers(-5, 0, 5)
    -5
    """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c