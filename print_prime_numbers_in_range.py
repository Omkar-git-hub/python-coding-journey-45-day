#!/usr/bin/env python3
"""
Print Prime Numbers in a Range

This script provides a utility to print all prime numbers within a given inclusive range.
It can be used as a module or run as a standalone script. When executed directly,
the user will be prompted to enter the start and end of the range.

Example:
    $ python print_prime_numbers_in_range.py
    Enter start of range: 10
    Enter end of range: 30
    11 13 17 19 23 29
"""

from __future__ import annotations


def is_prime(n: int) -> bool:
    """
    Determine whether a given integer is a prime number.

    Parameters
    ----------
    n : int
        The number to test for primality.

    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def print_prime_numbers_in_range(start: int, end: int) -> None:
    """
    Print all prime numbers in the inclusive range [start, end].

    Parameters
    ----------
    start : int
        The beginning of the range.
    end : int
        The end of the range.
    """
    if start > end:
        start, end = end, start

    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    print(" ".join(primes))


if __name__ == "__main__":
    try:
        start_input = input("Enter start of range: ")
        end_input = input("Enter end of range: ")
        start_val = int(start_input.strip())
        end_val = int(end_input.strip())
    except ValueError:
        print("Invalid input. Please enter integer values.")
        exit(1)

    print_prime_numbers_in_range(start_val, end_val)