"""
Print Numbers in a Range

This module provides a simple utility to print all integers within a
specified inclusive range. It can be used as a script (reading the
range from standard input) or imported and called directly.

Typical usage as a script:
    $ python print_numbers.py
    1
    5
    # (prints numbers from 1 to 5, each on its own line)

When imported:
    from print_numbers import print_numbers
    print_numbers(3, 7)  # prints 3,4,5,6,7 each on a new line
"""

from typing import Iterable


def _generate_range(start: int, end: int) -> Iterable[int]:
    """
    Generate an inclusive range of integers from ``start`` to ``end``.
    Handles cases where ``start`` is greater than ``end`` by counting
    downwards.

    Args:
        start: The first integer in the range.
        end: The last integer in the range.

    Yields:
        Each integer in the inclusive range.
    """
    step = 1 if start <= end else -1
    current = start
    while True:
        yield current
        if current == end:
            break
        current += step


def print_numbers(start: int, end: int) -> None:
    """
    Print all numbers from ``start`` to ``end`` inclusive, one per line.

    Args:
        start: The starting integer.
        end: The ending integer.
    """
    for number in _generate_range(start, end):
        print(number)


if __name__ == "__main__":
    try:
        # Expect two integers from standard input, each on its own line.
        s = int(input().strip())
        e = int(input().strip())
    except Exception as exc:
        raise ValueError("Two integer inputs are required.") from exc

    print_numbers(s, e)