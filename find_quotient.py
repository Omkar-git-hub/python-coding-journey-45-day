def find_quotient(dividend, divisor):
    """
    Calculate the quotient of two numbers.

    Parameters:
    dividend (int or float): The number to be divided.
    divisor (int or float): The number by which to divide.

    Returns:
    float: The result of dividend divided by divisor if divisor is not zero.
    None: If divisor is zero, indicating division cannot be performed.
    """
    if divisor == 0:
        return None
    else:
        return dividend / divisor