def join_strings(strings, separator=" "):
    """
    Join a list of strings into a single string with a given separator.

    Parameters:
    - strings (list of str): The list of strings to join.
    - separator (str): The separator to insert between strings. Defaults to a single space.

    Returns:
    - str: The concatenated string. Returns an empty string if the input list is empty.
    """
    if not isinstance(strings, list):
        raise TypeError("First argument must be a list of strings.")
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements in the list must be strings.")
    return separator.join(strings)


if __name__ == "__main__":
    # Example usage
    sample_list = ["Hello", "world", "from", "Python"]
    print(join_strings(sample_list))          # Default separator (space)
    print(join_strings(sample_list, ", "))    # Custom separator