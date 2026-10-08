"""
multiply_two_numbers.py

This module reads two numbers from standard input and prints their product.
It follows the same pattern as the existing add_two_numbers.py and
subtract_two_numbers.py modules in this repository.

The function `multiply_two_numbers` is the main entry point and is
executed when the module is run as a script.
"""

from read_two_numbers import read_two_numbers


def multiply_two_numbers() -> None:
    """
    Reads two numbers from input, multiplies them, and prints the result.

    The function uses `read_two_numbers` to obtain the input values.
    It then prints the product of the two numbers to standard output.
    """
    a, b = read_two_numbers()
    print(a * b)


if __name__ == "__main__":
    multiply_two_numbers()