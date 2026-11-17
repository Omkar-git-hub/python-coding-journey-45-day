"""
Demonstrates the use of the built‑in `filter` function in Python.

The module provides a small helper that filters even numbers from a list.
It mirrors the style of the existing `use_map_function.py` in the repository,
providing a clear example of how `filter` can be used in a functional
programming style.

Functions
---------
filter_even_numbers(numbers: list[int]) -> list[int]
    Return a new list containing only the even integers from *numbers*.
"""

from __future__ import annotations


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """
    Return a list of even numbers from the provided list.

    Parameters
    ----------
    numbers : list[int]
        The list of integers to filter.

    Returns
    -------
    list[int]
        A new list containing only the even integers from *numbers*.

    Examples
    --------
    >>> filter_even_numbers([1, 2, 3, 4, 5])
    [2, 4]
    """
    # Using filter with a lambda to keep only even numbers.
    return list(filter(lambda x: x % 2 == 0, numbers))


if __name__ == "__main__":
    # Simple demonstration when the module is run directly.
    sample_numbers = [10, 15, 20, 25, 30]
    print("Original list:", sample_numbers)
    print("Even numbers:", filter_even_numbers(sample_numbers))