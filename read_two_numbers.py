"""
Script to read two numbers from standard input and print their sum.

The script reads two lines from ``stdin``, converts them to numbers,
adds them using :func:`add_two_numbers`, and prints the result.
If the input cannot be parsed as numbers, an error message is printed.
"""

from __future__ import annotations

from typing import Tuple

from add_two_numbers import add_two_numbers


def _parse_input_line(line: str) -> float:
    """
    Convert a raw input line to a float.

    Strips whitespace and attempts to cast to ``float``. Raises ``ValueError``
    if conversion fails.
    """
    return float(line.strip())


def read_two_numbers() -> Tuple[float, float]:
    """
    Read two numeric values from standard input.

    Returns
    -------
    tuple(float, float)
        The two numbers entered by the user.

    Raises
    ------
    ValueError
        If either input line cannot be converted to a float.
    """
    first_line = input()
    second_line = input()
    a = _parse_input_line(first_line)
    b = _parse_input_line(second_line)
    return a, b


def main() -> None:
    """
    Entry point for the script.

    Reads two numbers, computes their sum using ``add_two_numbers`` and prints
    the result. If the input is invalid, prints an error message.
    """
    try:
        a, b = read_two_numbers()
    except ValueError:
        print("Invalid input")
        return

    result = add_two_numbers(a, b)

    # Print as int when the result is mathematically an integer
    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)


if __name__ == "__main__":
    main()