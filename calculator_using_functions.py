#!/usr/bin/env python3
"""
Calculator Using Functions

Provides basic arithmetic operations as separate functions and a
`calculate` helper that selects the appropriate operation based on an
operator string.

Supported operators:
    '+'  addition
    '-'  subtraction
    '*'  multiplication
    '/'  division (float division, raises ZeroDivisionError on division by zero)
    '**' exponentiation (power)

The module can also be executed directly to perform a calculation from
standard input:

    $ python calculator_using_functions.py 3 + 5
    8

If the operator is not recognised, a ValueError is raised.
"""

from __future__ import annotations
from typing import Callable


def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of *a* and *b* (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of *a* divided by *b*.

    Raises:
        ZeroDivisionError: If *b* is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return *a* raised to the power of *b*."""
    return a ** b


# Mapping of operator symbols to the corresponding function
_OPERATOR_MAP: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}


def calculate(a: float, b: float, operator: str) -> float:
    """
    Perform a calculation using the given *operator* on operands *a* and *b*.

    Args:
        a: First operand.
        b: Second operand.
        operator: A string representing the operation (e.g., '+', '-', '*', '/', '**').

    Returns:
        The result of the arithmetic operation.

    Raises:
        ValueError: If the operator is not supported.
        ZeroDivisionError: Propagated from :func:`divide` when dividing by zero.
    """
    if operator not in _OPERATOR_MAP:
        raise ValueError(f"Unsupported operator: {operator!r}")
    func = _OPERATOR_MAP[operator]
    return func(a, b)


def _parse_operand(value: str) -> float:
    """
    Convert a string to a float. Allows integer strings as well.
    """
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"Invalid numeric value: {value!r}") from exc


def _main() -> None:
    """
    Simple command‑line interface.

    Expected arguments: <number1> <operator> <number2>
    Example:
        python calculator_using_functions.py 10 / 2
    """
    import sys

    if len(sys.argv) != 4:
        prog = sys.argv[0]
        sys.stderr.write(f"Usage: {prog} <number1> <operator> <number2>\n")
        sys.exit(1)

    a_str, operator, b_str = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = _parse_operand(a_str)
        b = _parse_operand(b_str)
        result = calculate(a, b, operator)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)

    # Print result without unnecessary trailing .0 for whole numbers
    if result.is_integer():
        sys.stdout.write(str(int(result)))
    else:
        sys.stdout.write(str(result))


if __name__ == "__main__":
    _main()