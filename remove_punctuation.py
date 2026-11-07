"""
remove_punctuation.py

This module provides a utility function to remove all punctuation characters
from a given string. Punctuation characters are defined by the
`string.punctuation` constant from the standard library.

The function preserves all other characters, including whitespace and
Unicode characters that are not considered punctuation by the standard
library.

Example:
    >>> remove_punctuation("Hello, world!")
    'Hello world'
"""

import string
from typing import AnyStr


def remove_punctuation(text: AnyStr) -> AnyStr:
    """
    Remove all punctuation characters from the input string.

    Parameters
    ----------
    text : str
        The string from which punctuation should be removed.

    Returns
    -------
    str
        The input string with all punctuation characters removed.

    Notes
    -----
    - Punctuation characters are those defined in ``string.punctuation``.
    - The function does not modify whitespace or other non-punctuation
      characters.
    - The function accepts any string-like object that can be iterated over
      character by character. It returns a string.

    Examples
    --------
    >>> remove_punctuation("Hello, world!")
    'Hello world'
    >>> remove_punctuation("Python's awesome.")
    'Pythons awesome'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Using a generator expression for efficient filtering
    return ''.join(ch for ch in text if ch not in string.punctuation)