"""
Module providing a simple function to print a greeting message.
"""

def print_city() -> None:
    """
    Print a greeting message.

    This function prints "Hello World" to the standard output.
    It is intended to be used by the test suite to verify
    basic output functionality.
    """
    print("Hello World")

if __name__ == "__main__":
    print_city()