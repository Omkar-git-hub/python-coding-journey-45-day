"""
find_sum_of_odd_numbers.py

This module provides a single function, `find_sum_of_odd_numbers`, which
calculates the sum of all odd integers in a given iterable.

The implementation follows the same style as the existing
`find_sum_of_even_numbers.py` module in the repository, ensuring
consistency across the codebase.

Author: Senior Software Engineer
"""

from typing import Iterable, Union


def find_sum_of_odd_numbers(numbers: Iterable[Union[int, float]]) -> int:
    """
    Return the sum of all odd integers in the provided iterable.

    Parameters
    ----------
    numbers : Iterable[Union[int, float]]
        An iterable containing numeric values. Only integer values are
        considered for the sum; floating point numbers are ignored.

    Returns
    -------
    int
        The sum of all odd integers in the iterable. If no odd integers
        are present, returns 0.

    Examples
    --------
    >>> find_sum_of_odd_numbers([1, 2, 3, 4, 5])
    9
    >>> find_sum_of_odd_numbers([])
    0
    """
    total = 0
    for num in numbers:
        # Only integers contribute to the sum
        if isinstance(num, int) and num % 2 != 0:
            total += num
    return total


# Optional demonstration when run as a script
if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(f"Sum of odd numbers in {sample}: {find_sum_of_odd_numbers(sample)}")