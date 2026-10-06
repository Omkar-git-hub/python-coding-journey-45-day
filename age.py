"""
Module for printing the user's age.

This module provides a simple function `print_age` that takes an integer
representing an age and prints it to standard output. The function is
intended to be used in educational exercises where the user is asked to
output their age.

Example
-------
>>> from age import print_age
>>> print_age(30)
30
"""

def print_age(age: int) -> None:
    """
    Print the given age to standard output.

    Parameters
    ----------
    age : int
        The age to print. It is expected to be a non-negative integer.

    Returns
    -------
    None
    """
    print(age)