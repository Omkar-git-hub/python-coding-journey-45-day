"""
count_characters.py

This module provides a utility function to count the occurrences of each character in a given string.
The function returns a dictionary where keys are characters and values are the number of times
each character appears in the input string.

The implementation is straightforward and works for any string, including those containing
Unicode characters. It does not ignore whitespace or punctuation unless explicitly filtered
by the caller.

Example usage:
>>> count_characters("hello world")
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

from collections import Counter
from typing import Dict


def count_characters(text: str) -> Dict[str, int]:
    """
    Count the occurrences of each character in the provided string.

    Parameters
    ----------
    text : str
        The string to analyze.

    Returns
    -------
    Dict[str, int]
        A dictionary mapping each character to its count in the string.
        If the input string is empty, an empty dictionary is returned.

    Notes
    -----
    - The function is case-sensitive; 'A' and 'a' are considered distinct.
    - All characters, including whitespace and punctuation, are counted.
    """
    if not text:
        return {}

    # Using Counter for efficient counting
    return dict(Counter(text))


# If this module is executed as a script, demonstrate the function with a simple example.
if __name__ == "__main__":
    sample = "Hello, World!"
    print(f"Input string: {sample!r}")
    print("Character counts:")
    for char, count in sorted(count_characters(sample).items()):
        print(f"  {char!r}: {count}")