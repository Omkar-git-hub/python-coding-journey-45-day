def compare_two_strings(str1: str, str2: str) -> bool:
    """
    Compare two strings for equality.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if both strings are exactly the same, False otherwise.
    """
    return str1 == str2


if __name__ == "__main__":
    # Simple CLI for manual testing
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    if compare_two_strings(first, second):
        print("Strings are equal")
    else:
        print("Strings are not equal")