"""
Reverse a Number

This module provides a single function `reverse_number` that takes an integer
and returns its digits reversed. The sign of the input number is preserved.
"""

def reverse_number(number: int) -> int:
    """
    Reverse the digits of an integer.

    Parameters
    ----------
    number : int
        The integer to reverse.

    Returns
    -------
    int
        The integer obtained by reversing the digits of `number`. The sign
        of the original number is preserved.

    Examples
    --------
    >>> reverse_number(12345)
    54321
    >>> reverse_number(-987)
    -789
    >>> reverse_number(0)
    0
    """
    # Preserve the sign
    sign = -1 if number < 0 else 1
    number_abs = abs(number)

    # Reverse the digits using arithmetic
    reversed_abs = 0
    while number_abs > 0:
        reversed_abs = reversed_abs * 10 + number_abs % 10
        number_abs //= 10

    return sign * reversed_abs