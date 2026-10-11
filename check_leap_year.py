"""
check_leap_year.py

Utility to determine whether a given year is a leap year.

The module exposes a single function `check_leap_year(year: int) -> bool`
which returns True if the year is a leap year according to the Gregorian
calendar rules, otherwise False.

When executed as a script, the module reads an integer from standard
input and prints "Leap year" or "Not a leap year" accordingly.
"""

def check_leap_year(year: int) -> bool:
    """
    Determine if the specified year is a leap year.

    A year is a leap year if it is divisible by 4, except for years
    divisible by 100 unless they are also divisible by 400.

    Parameters
    ----------
    year : int
        The year to evaluate.

    Returns
    -------
    bool
        True if the year is a leap year, False otherwise.
    """
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0


if __name__ == "__main__":
    import sys

    try:
        input_year = int(sys.stdin.readline().strip())
    except (ValueError, TypeError):
        print("Invalid input. Please provide an integer year.")
        sys.exit(1)

    if check_leap_year(input_year):
        print("Leap year")
    else:
        print("Not a leap year")