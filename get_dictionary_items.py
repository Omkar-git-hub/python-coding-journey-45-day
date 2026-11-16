"""
Get Dictionary Items

This module provides a single utility function that returns the items
of a dictionary as a list of (key, value) tuples. The function is
intended to be used in scripts and tests that need to inspect the
contents of a dictionary in a predictable order.

Example
-------
>>> sample = {'a': 1, 'b': 2}
>>> get_dictionary_items(sample)
[('a', 1), ('b', 2)]
"""

def get_dictionary_items(dictionary):
    """
    Return the items of the provided dictionary as a list of tuples.

    Parameters
    ----------
    dictionary : dict
        The dictionary whose items are to be retrieved.

    Returns
    -------
    list of tuple
        A list containing all key-value pairs from the dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Expected a dictionary, got %s" % type(dictionary).__name__)
    return list(dictionary.items())