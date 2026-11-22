def float_to_integer(value):
    """
    Converts a float (or a string representing a float) to an integer by truncating
    the decimal part.

    Raises:
        ValueError: If the value cannot be converted to an integer.
    """
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid float value for conversion to integer: {value!r}") from e