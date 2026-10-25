"""
find_missing_number.py

This module provides a utility function to find the missing number in a list
containing distinct integers from 1 to n with exactly one number missing.

The implementation uses the arithmetic series sum formula to compute the
expected sum of numbers from 1 to n and subtracts the actual sum of the
provided list. This approach runs in O(n) time and O(1) additional space.

Author: Senior Software Engineer
"""

from __future__ import annotations

__all__ = ["find_missing_number"]


def find_missing_number(numbers: list[int]) -> int:
    """
    Find the missing number in a list of distinct integers ranging from 1 to n.

    The list is expected to contain all numbers from 1 to n except one missing
    number. The function calculates the expected sum of the full range using
    the arithmetic series formula and subtracts the sum of the provided list
    to determine the missing value.

    Parameters
    ----------
    numbers : list[int]
        A list of distinct integers from 1 to n with one number missing.

    Returns
    -------
    int
        The missing number in the sequence.

    Raises
    ------
    ValueError
        If the input list is empty or if the list does not represent a valid
        sequence from 1 to n with exactly one missing element.

    Examples
    --------
    >>> find_missing_number([1, 2, 4, 5])
    3
    >>> find_missing_number([2, 3, 4, 5])
    1
    >>> find_missing_number([1, 2, 3, 4])
    5
    """
    if not numbers:
        raise ValueError("Input list must contain at least one element.")

    # The length of the full sequence is one more than the length of the list.
    n = len(numbers) + 1

    # Validate that all numbers are within the expected range.
    if any(num < 1 or num > n for num in numbers):
        raise ValueError(
            f"All numbers must be in the range 1 to {n} inclusive."
        )

    # Compute expected sum of 1..n using the arithmetic series formula.
    expected_sum = n * (n + 1) // 2

    # Compute actual sum of the provided numbers.
    actual_sum = sum(numbers)

    missing = expected_sum - actual_sum

    # The missing number must be within the valid range.
    if missing < 1 or missing > n:
        raise ValueError("Input list does not represent a valid sequence with one missing number.")

    return missing