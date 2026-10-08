"""
calculate_power.py

This module provides a simple utility function to calculate the power of a number.
"""

def calculate_power(base: float | int, exponent: float | int) -> float | int:
    """
    Calculate the power of a number.

    Parameters
    ----------
    base : float | int
        The base number.
    exponent : float | int
        The exponent to raise the base to.

    Returns
    -------
    float | int
        The result of base raised to the power of exponent.

    Examples
    --------
    >>> calculate_power(2, 3)
    8
    >>> calculate_power(5, 0)
    1
    >>> calculate_power(9, 0.5)
    3.0
    """
    return base ** exponent


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python calculate_power.py <base> <exponent>")
        sys.exit(1)

    try:
        base = float(sys.argv[1])
        exponent = float(sys.argv[2])
    except ValueError:
        print("Both base and exponent must be numbers.")
        sys.exit(1)

    result = calculate_power(base, exponent)
    print(result)