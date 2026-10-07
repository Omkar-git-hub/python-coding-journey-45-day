"""Module that defines and prints an age value.

This module demonstrates a simple use of a global variable and a
function that prints that variable.  The value is intentionally
chosen to be a small integer so that the tests can easily verify
the output.

The module can be executed directly, in which case the :func:`main`
function will run and print the age to standard output.
"""

# The age value used throughout the project.
age: int = 30

def main() -> None:
    """Print the age in a human‑readable format."""
    # Using an f‑string keeps the code concise and readable.
    print(f"Age: {age}")

# Allow the module to be run as a script.
if __name__ == "__main__":
    main()