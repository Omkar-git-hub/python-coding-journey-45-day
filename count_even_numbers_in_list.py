"""
count_even_numbers_in_list.py

This module provides a single function, `count_even_numbers_in_list`, which
returns the number of even integers present in a given list. The function
is intentionally lightweight and type-agnostic: it accepts any iterable
of numbers and counts those that are integers and divisible by two.

The implementation follows the style of the existing repository:
- A clear, descriptive function name.
- Type hints for better static analysis.
- A concise, readable implementation.
- A small docstring explaining behaviour and edge cases.

The function is pure and has no side effects, making it suitable for
unit testing and reuse in other modules.
"""

from __future__ import annotations

from typing import Iterable, Sequence, Union


def count_even_numbers_in_list(numbers: Union[Sequence[int], Iterable[int]]) -> int:
    """
    Count the number of even integers in the provided sequence or iterable.

    Parameters
    ----------
    numbers : Union[Sequence[int], Iterable[int]]
        A sequence or iterable of integers. Non-integer values are ignored.

    Returns
    -------
    int
        The count of even integers in `numbers`.

    Examples
    --------
    >>> count_even_numbers_in_list([1, 2, 3, 4, 5])
    2
    >>> count_even_numbers_in_list([])
    0
    >>> count_even_numbers_in_list([0, -2, 7, 8])
    3
    """
    # Using a generator expression keeps memory usage minimal
    return sum(1 for n in numbers if isinstance(n, int) and n % 2 == 0)


# If the module is executed directly, demonstrate the function with a simple example.
if __name__ == "__main__":
    import sys

    # Attempt to read a comma-separated list of integers from the command line.
    if len(sys.argv) > 1:
        try:
            input_numbers = [int(item) for item in sys.argv[1].split(",")]
        except ValueError:
            print("Please provide a comma-separated list of integers.")
            sys.exit(1)
    else:
        input_numbers = [1, 2, 3, 4, 5]  # Default example

    count = count_even_numbers_in_list(input_numbers)
    print(f"Even numbers count: {count}")