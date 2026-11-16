"""
clear_set.py

This module provides a simple utility function to clear all elements from a set.
"""

def clear_set(s: set) -> set:
    """
    Clears all elements from the provided set and returns the cleared set.

    Parameters
    ----------
    s : set
        The set to be cleared.

    Returns
    -------
    set
        The cleared set (which will be empty).
    """
    s.clear()
    return s


if __name__ == "__main__":
    # Demo usage
    sample_set = {1, 2, 3, 4, 5}
    print(f"Original set: {sample_set}")
    cleared = clear_set(sample_set)
    print(f"Cleared set: {cleared}")