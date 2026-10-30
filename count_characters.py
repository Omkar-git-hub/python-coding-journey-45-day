def count_characters(string: str) -> dict:
    """
    Count the frequency of each character in the given string.

    Parameters
    ----------
    string : str
        The string whose characters are to be counted.

    Returns
    -------
    dict
        A dictionary where keys are characters and values are the number of
        times each character appears in the string.
    """
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(count_characters(user_input))