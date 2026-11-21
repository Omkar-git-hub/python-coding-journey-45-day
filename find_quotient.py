def find_quotient(dividend, divisor):
    """
    Find the integer quotient of two numbers and handle division by zero.

    Parameters:
        dividend (int): The number to be divided.
        divisor (int): The number to divide by.

    Returns:
        int or None: The integer quotient (using floor division), or None if divisor is zero.
    """
    if divisor == 0:
        print("Error: Division by zero")
        return None
    return dividend // divisor