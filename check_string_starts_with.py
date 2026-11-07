"""
check_string_starts_with.py

This module provides a utility function to determine whether a given string
starts with a specified substring.

The function is intentionally simple and follows the conventions used
throughout the repository: it accepts two string arguments and returns a
boolean value.  It also performs basic type checking to ensure that
both arguments are strings, raising a TypeError if not.  This mirrors the
behaviour of many other helper functions in the project.

Author: Senior Software Engineer
"""

def check_string_starts_with(string: str, start: str) -> bool:
    """
    Return True if `string` starts with the substring `start`, otherwise False.

    Parameters
    ----------
    string : str
        The string to be examined.
    start : str
        The substring to check for at the beginning of `string`.

    Returns
    -------
    bool
        True if `string` begins with `start`, False otherwise.

    Raises
    ------
    TypeError
        If either `string` or `start` is not a string.
    """
    if not isinstance(string, str) or not isinstance(start, str):
        raise TypeError("Both arguments must be strings.")

    return string.startswith(start)