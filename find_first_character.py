def find_first_character(s: str) -> str:
    """
    Return the first character of the given string.

    If the string is empty, an empty string is returned.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The first character of the string, or an empty string if the input is empty.
    """
    return s[0] if s else ""


if __name__ == "__main__":
    user_input = input()
    print(find_first_character(user_input))