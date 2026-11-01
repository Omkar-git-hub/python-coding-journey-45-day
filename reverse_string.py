def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return s[::-1]


if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    print(reverse_string(user_input))