"""
Remove Duplicate Characters

This module provides a function to remove duplicate characters from a string,
preserving the order of their first occurrence.

Example:
    >>> remove_duplicate_characters("programming")
    'progamin'
"""

def remove_duplicate_characters(s: str) -> str:
    """
    Return a new string with duplicate characters removed, preserving the original order.

    Parameters
    ----------
    s : str
        The input string from which duplicates should be removed.

    Returns
    -------
    str
        A string containing only the first occurrence of each character from the input.
    """
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    # Simple command‑line interface for manual testing.
    import sys

    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    else:
        input_str = input("Enter a string: ")

    print(remove_duplicate_characters(input_str))