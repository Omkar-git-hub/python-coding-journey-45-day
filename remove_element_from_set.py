"""
remove_element_from_set.py

This module provides a utility function to remove an element from a set.
The function is designed to be safe: it will not raise an exception if the
element is not present in the set. It simply returns the set unchanged in
that case.

Author: Senior Software Engineer
"""

from __future__ import annotations

def remove_element_from_set(s: set, element) -> set:
    """
    Remove an element from a set if it exists.

    Parameters
    ----------
    s : set
        The set from which the element should be removed.
    element : Any
        The element to remove from the set.

    Returns
    -------
    set
        The set after attempting to remove the element. The original set
        is modified in place and also returned for convenience.

    Examples
    --------
    >>> my_set = {1, 2, 3}
    >>> remove_element_from_set(my_set, 2)
    {1, 3}
    >>> remove_element_from_set(my_set, 5)
    {1, 3}
    """
    # Use discard to avoid KeyError if element is not present
    s.discard(element)
    return s