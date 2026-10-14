def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters
    ----------
    n : int
        The number to calculate the factorial for. Must be a non-negative integer.

    Returns
    -------
    int
        The factorial of n.

    Raises
    ------
    TypeError
        If n is not an integer.
    ValueError
        If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result