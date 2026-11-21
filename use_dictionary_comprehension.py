"""
Demonstrates the use of dictionary comprehension in Python.

This module provides a simple example of creating a dictionary from a list
of numbers where each key is the number and each value is its square.
It also shows how to filter a dictionary using a comprehension.

Functions
---------
create_square_dict(numbers)
    Returns a dictionary mapping each number in the list to its square.

filter_even_keys(d)
    Returns a new dictionary containing only the items from `d` whose keys are even.
"""

def create_square_dict(numbers):
    """
    Create a dictionary where each key is a number from the input list and
    each value is the square of that number.

    Parameters
    ----------
    numbers : list[int]
        A list of integers.

    Returns
    -------
    dict[int, int]
        Dictionary mapping each number to its square.
    """
    return {n: n * n for n in numbers}


def filter_even_keys(d):
    """
    Return a new dictionary containing only the items from `d` whose keys are even.

    Parameters
    ----------
    d : dict[int, any]
        Input dictionary.

    Returns
    -------
    dict[int, any]
        Dictionary with only even-numbered keys.
    """
    return {k: v for k, v in d.items() if k % 2 == 0}


if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    squares = create_square_dict(numbers)
    print("Square dictionary:", squares)

    filtered = filter_even_keys(squares)
    print("Filtered even-key dictionary:", filtered)