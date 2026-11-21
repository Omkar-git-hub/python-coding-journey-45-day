def divide_two_numbers(a, b):
    """
    Divide two numbers and handle division by zero.

    Parameters:
        a (int or float): Numerator.
        b (int or float): Denominator.

    Returns:
        float or None: The result of a / b, or None if b is zero.
    """
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b