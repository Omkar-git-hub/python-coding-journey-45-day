"""
Read Two Numbers

This script reads two numbers from standard input, one per line,
converts them to integers, and prints their sum.

The script is designed to be used in a command-line environment
where the user provides the two numbers interactively or via
input redirection.

Example:
    $ python read_two_numbers.py
    3
    5
    8
"""

def main() -> None:
    """
    Reads two integers from input and prints their sum.

    Raises:
        ValueError: If the input cannot be converted to an integer.
    """
    try:
        first_input = input()
        second_input = input()
        first_number = int(first_input.strip())
        second_number = int(second_input.strip())
        print(first_number + second_number)
    except ValueError as exc:
        # If the input is not a valid integer, we raise a clear error.
        raise ValueError("Both inputs must be valid integers.") from exc

if __name__ == "__main__":
    main()