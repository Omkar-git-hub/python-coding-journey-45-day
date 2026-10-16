def reverse_string(s: str) -> str:
    """
    Return the reversed version of the input string.

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
    # Simple command‑line usage: read a line from stdin and print its reverse.
    try:
        input_str = input()
    except EOFError:
        input_str = ""
    print(reverse_string(input_str))