def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer n using a while loop.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result