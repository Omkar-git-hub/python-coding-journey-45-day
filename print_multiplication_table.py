"""
Print Multiplication Table

This module provides a single function `print_multiplication_table` that prints
the multiplication table for a given integer from 1 to 10 inclusive.

The output format for each line is:
    <multiplier> * <number> = <product>

Each line is printed to standard output followed by a newline.
"""

def print_multiplication_table(number: int) -> None:
    """
    Print the multiplication table for the given number from 1 to 10.

    Parameters
    ----------
    number : int
        The integer for which the multiplication table is printed.

    Returns
    -------
    None
    """
    for multiplier in range(1, 11):
        product = multiplier * number
        print(f"{multiplier} * {number} = {product}")