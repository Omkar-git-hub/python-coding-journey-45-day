"""
clear_dictionary.py

This module provides a simple utility function to clear all items from a dictionary.
"""

def clear_dictionary(dictionary: dict) -> dict:
    """
    Remove all items from the provided dictionary.

    Parameters
    ----------
    dictionary : dict
        The dictionary to be cleared.

    Returns
    -------
    dict
        The cleared dictionary (which will be empty).
    """
    dictionary.clear()
    return dictionary