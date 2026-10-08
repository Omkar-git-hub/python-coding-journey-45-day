"""
Module: number_to_string
Author: Senior Software Engineer
Description:
    Provides a utility function to convert numeric values (integers or floats)
    into their string representation. The function is intentionally simple
    but includes type validation to ensure that only numeric types are
    accepted, raising a TypeError otherwise.

    This module follows the project's existing style and conventions:
    - Uses type hints for clarity.
    - Provides a clear docstring for the public function.
    - Exposes the function via __all__ for explicit imports.
"""

from __future__ import annotations

from typing import Union

__all__ = ["number_to_string"]


def number_to_string(value: Union[int, float]) -> str:
    """
    Convert a numeric value to its string representation.

    Parameters
    ----------
    value : int | float
        The numeric value to convert. Only integers and floats are accepted.

    Returns
    -------
    str
        The string representation of the input number.

    Raises
    ------
    TypeError
        If *value* is not an instance of int or float.

    Examples
    --------
    >>> number_to_string(42)
    '42'
    >>> number_to_string(-3.14)
    '-3.14'
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"number_to_string expects an int or float, got {type(value).__name__}"
        )
    return str(value)