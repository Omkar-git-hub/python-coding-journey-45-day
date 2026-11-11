"""
Check Element in List

This module provides a simple utility function to determine whether a given
element exists within a list.

Functions
---------
check_element_in_list(lst, element)
    Returns True if element is present in lst, otherwise False.
"""

def check_element_in_list(lst, element):
    """
    Check if an element exists in a list.

    Parameters
    ----------
    lst : list
        The list to search.
    element : Any
        The element to look for.

    Returns
    -------
    bool
        True if element is found in lst, False otherwise.
    """
    return element in lst