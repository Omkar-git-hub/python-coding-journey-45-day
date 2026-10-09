"""
check_divisible_by_5.py

Provides a simple utility to determine whether a given integer is divisible by 5.

The function `check_divisible_by_5` returns a boolean value:
- `True` if the number is divisible by 5 (i.e., the remainder of the division by 5 is zero).
- `False` otherwise.

This module follows the same lightweight style as the other utility modules in the repository.
"""

def check_divisible_by_5(number: int) -> bool:
    """
    Determine if the provided integer is divisible by 5.

    Parameters
    ----------
    number : int
        The integer to test for divisibility by 5.

    Returns
    -------
    bool
        True if `number` is divisible by 5, False otherwise.
    """
    return number % 5 == 0