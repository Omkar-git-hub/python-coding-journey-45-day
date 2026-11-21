import math

def calculate_power(base, exponent):
    """
    Calculate the power of a number using the math module.

    Args:
        base (int | float): The base number.
        exponent (int | float): The exponent to raise the base to.

    Returns:
        int | float: The result of base raised to the power of exponent.
                     Returns an int when both inputs are ints and the
                     result is mathematically integral; otherwise returns a float.
    """
    result = math.pow(base, exponent)
    if isinstance(base, int) and isinstance(exponent, int):
        if result.is_integer():
            return int(result)
    return result