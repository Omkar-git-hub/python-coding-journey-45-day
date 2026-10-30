"""
find_most_frequent_character.py

This module provides a single function, `find_most_frequent_character`, which
returns the character that occurs most frequently in a given string.  If the
string is empty, an empty string is returned.  In the case of a tie, the
character that appears first in the original string is returned.

The implementation is straightforward and uses a dictionary to count
occurrences.  It is intentionally lightweight and has no external
dependencies, making it suitable for inclusion in the existing repository
without altering its behaviour or structure.
"""

from __future__ import annotations


def find_most_frequent_character(s: str) -> str:
    """
    Return the most frequent character in the given string.

    Parameters
    ----------
    s : str
        The input string to analyze.

    Returns
    -------
    str
        The character that appears most frequently in *s*.  If *s* is empty,
        an empty string is returned.  In the event of a tie, the first
        character that reaches the maximum frequency in the original string
        order is returned.

    Examples
    --------
    >>> find_most_frequent_character("hello")
    'l'