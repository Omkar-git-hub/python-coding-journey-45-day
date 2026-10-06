"""
Module to print the user's city.

This module provides a single function, `print_city`, which prints the
city name to standard output. The city is hard-coded to a default value
but can be easily modified if needed.

The function returns the city name for convenience, although the tests
only check the printed output.
"""

def print_city():
    """
    Print the city name to standard output.

    Returns:
        str: The name of the city that was printed.
    """
    city = "New York"
    print(f"City: {city}")
    return city

__all__ = ["print_city"]