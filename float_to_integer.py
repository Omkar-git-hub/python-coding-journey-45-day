# float_to_integer.py
# Converts a float to an integer by truncating the decimal part.

def float_to_integer(f: float) -> int:
    """Converts a float to an integer by truncating the decimal part.

    Args:
        f: The float value to convert.

    Returns:
        The integer part of the float.
    """
    return int(f