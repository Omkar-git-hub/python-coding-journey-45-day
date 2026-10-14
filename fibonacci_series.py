#!/usr/bin/env python3
"""
Generate Fibonacci Series

This script reads an integer ``n`` from standard input and prints the first ``n``
terms of the Fibonacci series separated by a single space.

If ``n`` is less than or equal to zero, nothing is printed.

Example
-------
Input:
    7

Output:
    0 1 1 2 3 5 8
"""

def generate_fibonacci(n: int):
    """Return a list containing the first ``n`` Fibonacci numbers.

    The series starts with 0, 1, ...

    Args:
        n: Number of terms to generate. Must be non‑negative.

    Returns:
        List[int]: Fibonacci numbers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def main():
    try:
        user_input = input().strip()
        n = int(user_input)
    except Exception:
        # If input is invalid, do nothing
        return

    series = generate_fibonacci(n)
    if series:
        print(" ".join(map(str, series)))

if __name__ == "__main__":
    main()