def string_to_integer(s):
    """
    Converts a numeric string to an integer.

    Raises:
        ValueError: If the string cannot be converted to an integer.
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid integer string: {s!r}") from e