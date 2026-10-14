"""
calculate_product_from_1_to_n.py

This module provides a single function `calculate_product_from_1_to_n` that
returns the product of all integers from 1 to a given positive integer `n`
(inclusive).  The implementation follows the same style as the other
utility modules in the repository.

Examples
--------
>>> calculate_product_from_1_to_n(5)
120

>>> calculate_product_from_1_to_n(0)
0

The function is intentionally simple and does not perform extensive
input validation beyond ensuring that the argument is an integer.  It
mirrors the behaviour of the existing `calculate_sum_from_1_to_n` module
in the repository, which returns 0 for a non‑positive input.
"""

def calculate_product_from_1_to_n(n: int) -> int:
    """
    Calculate the product of all integers from 1 to `n` inclusive.

    Parameters
    ----------
    n : int
        The upper bound of the product sequence.  If `n` is less than or
        equal to 0, the function returns 0.

    Returns
    -------
    int
        The product of the sequence 1 * 2 * ... * n, or 0 if `n` <= 0.

    Notes
    -----
    The implementation uses a simple iterative loop to avoid recursion
    depth issues for large `n`.  The function is deliberately kept
    lightweight to match the style of the other arithmetic utilities
    in the repository.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return 0

    product = 1
    for i in range(1, n + 1):
        product *= i

    return product


# If this module is executed as a script, demonstrate its usage.
if __name__ == "__main__":
    import sys

    try:
        n_value = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide a valid integer argument.")
        sys.exit(1)

    result = calculate_product_from_1_to_n(n_value)
    print(f"The product of numbers from 1 to {n_value} is {result}")