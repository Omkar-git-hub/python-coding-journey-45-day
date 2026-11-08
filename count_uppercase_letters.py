def count_uppercase_letters(s: str) -> int:
    """
    Count the number of uppercase letters in a given string.

    Parameters
    ----------
    s : str
        The string to analyze.

    Returns
    -------
    int
        The count of uppercase alphabetic characters in the string.
    """
    return sum(1 for char in s if char.isupper())