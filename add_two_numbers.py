"""
Utility module to add two numbers.

Provides a single function `add_two_numbers` that returns the sum of two
numeric values. The function accepts integers or floats and raises a
`TypeError` if either argument is not a number.
"""

from typing import Union

Number = Union[int, float]


def add_two_numbers(a: Number, b: Number) -> Number:
    """
    Return the sum of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        First addend.
    b : int or float
        Second addend.

    Returns
    -------
    int or float
        The arithmetic sum of ``a`` and ``b``.

    Raises
    ------
    TypeError
        If either ``a`` or ``b`` is not an ``int`` or ``float``.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be int or float, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be int or float, got {type(b).__name__}")
    return a + b