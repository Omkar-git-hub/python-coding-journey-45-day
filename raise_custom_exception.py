from custom_exception import MyCustomError

def raise_custom_exception(value):
    """
    Raises MyCustomError if the provided value is negative.

    Args:
        value (int or float): The numeric value to check.

    Raises:
        MyCustomError: If value is less than zero.
    """
    if value < 0:
        raise MyCustomError(f"Negative value encountered: {value}")
    return value