def convert_to_lowercase(string: str) -> str:
    """
    Convert the given string to lowercase.

    Args:
        string (str): The string to convert.

    Returns:
        str: The lowercase version of the input string.
    """
    return string.lower()


if __name__ == "__main__":
    user_input = input()
    print(convert_to_lowercase(user_input))