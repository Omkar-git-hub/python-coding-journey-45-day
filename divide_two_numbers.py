"""
Divide Two Numbers

This module provides a simple function to divide two numbers with basic
validation. It also includes a small command-line interface that reads two
numbers from standard input and prints the result.

Author: OpenAI ChatGPT
"""

def divide_two_numbers(dividend, divisor):
    """
    Divide two numbers and return the result.

    Parameters
    ----------
    dividend : int | float
        The number to be divided.
    divisor : int | float
        The number by which to divide.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ValueError
        If the divisor is zero.
    TypeError
        If either argument is not a number.
    """
    # Validate types
    if not isinstance(dividend, (int, float)):
        raise TypeError(f"Dividend must be a number, got {type(dividend).__name__}")
    if not isinstance(divisor, (int, float)):
        raise TypeError(f"Divisor must be a number, got {type(divisor).__name__}")

    # Validate divisor is not zero
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    return dividend / divisor


def _main():
    """
    Simple command-line interface for dividing two numbers.

    The user is prompted to enter two numbers. The result is printed to
    standard output. Any errors are reported to the user.
    """
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return

    try:
        result = divide_two_numbers(dividend, divisor)
    except Exception as exc:
        print(f"Error: {exc}")
        return

    print(f"{dividend} / {divisor} = {result}")


if __name__ == "__main__":
    _main()