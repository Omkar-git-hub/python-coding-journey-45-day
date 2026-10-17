"""
Convert a given string to uppercase.

This module provides a single function, `convert_to_uppercase`, which takes a string
as input and returns a new string with all characters converted to uppercase.
"""

def convert_to_uppercase(text: str) -> str:
    """
    Convert the provided string to uppercase.

    Parameters
    ----------
    text : str
        The string to convert.

    Returns
    -------
    str
        The uppercase version of the input string.

    Examples
    --------
    >>> convert_to_uppercase('hello')
    'HELLO'
    >>> convert_to_uppercase('Python 3.8')
    'PYTHON 3.8'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()