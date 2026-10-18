def remove_spaces_from_string(s: str) -> str:
    """
    Remove all space characters from the given string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The string with all spaces removed.
    """
    return s.replace(" ", "")


if __name__ == "__main__":
    user_input = input()
    print(remove_spaces_from_string(user_input))