"""
Module to convert string representations of numbers to integers.
"""


def convert_string_to_integer(value: str) -> int:
    """
    Convert a string to an integer.

    Args:
        value: The string to convert.

    Returns:
        The integer value of the string.

    Raises:
        ValueError: If the string cannot be converted to an integer.
    """
    return int(value)


def safe_convert_string_to_integer(value: str, default: int = 0) -> int:
    """
    Safely convert a string to an integer, returning a default value on failure.

    Args:
        value: The string to convert.
        default: The value to return if conversion fails.

    Returns:
        The integer value of the string, or the default value if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default