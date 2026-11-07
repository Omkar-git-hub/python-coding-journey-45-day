def check_string_ends_with(string: str, suffix: str) -> bool:
    """
    Check if the given string ends with the specified suffix.

    Args:
        string (str): The string to be checked.
        suffix (str): The suffix to look for.

    Returns:
        bool: True if `string` ends with `suffix`, otherwise False.
    """
    return string.endswith(suffix)


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    input_suffix = input("Enter suffix to check: ")
    result = check_string_ends_with(input_string, input_suffix)
    print(result)