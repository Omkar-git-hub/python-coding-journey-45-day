#!/usr/bin/env python3
"""
Print Inverted Triangle

This script prints an inverted right‑angled triangle of asterisks.
By default it prints a triangle with 5 rows, but the number of rows
can be overridden by passing a different integer to the function.

Example output for the default 5 rows:

*****
****
***
**
*

"""

def print_inverted_triangle(rows: int = 5) -> None:
    """
    Print an inverted right‑angled triangle of asterisks.

    Parameters
    ----------
    rows : int, optional
        Number of rows in the triangle. Must be a positive integer.
        Default is 5.

    Returns
    -------
    None
    """
    if rows <= 0:
        raise ValueError("Number of rows must be a positive integer")

    for i in range(rows, 0, -1):
        print('*' * i)


if __name__ == "__main__":
    # Default behaviour: print a 5‑row inverted triangle
    print_inverted_triangle()