"""
count_characters.py

Provides a simple utility to count the number of characters in a string.
"""

def count_characters(s: str) -> int:
    """
    Return the number of characters in the given string.

    Parameters
    ----------
    s : str
        The string whose characters are to be counted.

    Returns
    -------
    int
        The total number of characters in the string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return len(s)

if __name__ == "__main__":
    # Simple demonstration when run as a script
    import sys
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
        print(f"Number of characters in '{input_str}': {count_characters(input_str)}")
    else:
        print("Usage: python count_characters.py <string>")