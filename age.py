"""
Module for printing a user's age.

This module provides a single public function, :func:`print_age`, which
prints a formatted string containing the age supplied by the caller.
The function is intentionally simple to keep the focus on the
exercise of writing clean, testable code.

Example
-------
>>> from age import print_age
>>> print_age(30)
Your age is 30
"""

from __future__ import annotations

__all__ = ["print_age"]


def print_age(age: int) -> None:
    """
    Print the user's age in a human‑readable format.

    Parameters
    ----------
    age : int
        The age to display.  The function does not perform any
        validation beyond the type hint; callers should ensure that
        ``age`` is an integer.

    Returns
    -------
    None
        The function prints directly to standard output and returns
        ``None``.
    """
    print(f"Your age is {age}")