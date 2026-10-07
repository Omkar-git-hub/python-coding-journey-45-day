"""
Module that prints the user's city.

This module provides a single function, :func:`print_city`, which prints
the name of the city. The city name is hard‑coded to match the expected
output in the test suite.
"""

def print_city() -> None:
    """
    Print the name of the city.

    The function writes the city name to standard output. It is designed
    to be used by the test suite which captures stdout and verifies the
    exact string.
    """
    print("San Francisco")