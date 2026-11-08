"""
split_string.py

This module provides a simple utility function to split a string into a list
of substrings based on a specified delimiter. The default delimiter is a
single space, which splits the string into words.

Author: Senior Software Engineer
"""

def split_string(s: str, delimiter: str = " ") -> list[str]:
    """
    Split the input string `s` into a list of substrings using the provided
    `delimiter`.

    Parameters
    ----------
    s : str
        The string to split.
    delimiter : str, optional
        The delimiter to use for splitting. Defaults to a single space.

    Returns
    -------
    list[str]
        A list containing the split substrings.

    Examples
    --------
    >>> split_string("Hello World")
    ['Hello', 'World']

    >>> split_string("a,b,c", ",")
    ['a', 'b', 'c']

    >>> split_string("one two three", " ")
    ['one', 'two', 'three']
    """
    # Using the built-in str.split method ensures efficient and reliable
    # splitting behavior, handling edge cases such as consecutive delimiters
    # and leading/trailing delimiters according to Python's standard.
    return s.split(delimiter)


if __name__ == "__main__":
    # Demo usage
    sample = "Hello World, this is a test."
    print(f"Original string: {sample}")
    print(f"Split by space: {split_string(sample)}")
    print(f"Split by comma and space: {split_string(sample, ', ')}")