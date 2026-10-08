"""Script that prints a friendly greeting.

Running this module as a script will output the classic
``Hello, World!`` message.  The :func:`main` function is kept
separate from the top‑level code to make the module easier to
test and reuse programmatically.
"""

def main() -> None:
    """Print a greeting message to standard output."""
    print("Hello, World!")

# Execute the greeting when the module is run directly.
if __name__ == "__main__":
    main()