"""
Module for printing a person's age.

This module provides a simple function that prints the age
in a human‑readable format.  The function is intentionally
minimal to keep the repository lightweight and to serve as
an example for the "Print Your Age" exercise.

Example
-------
>>> from age import print_age
>>> print_age(30)
Age: 30
"""

def print_age(age: int) -> None:
    """
    Print the given age in a formatted string.

    Parameters
    ----------
    age : int
        The age to print.  It is expected to be a non‑negative integer.

    Returns
    -------
    None
        The function prints directly to standard output and returns
        ``None``.
    """
    print(f"Age: {age}")