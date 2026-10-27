def find_set_difference(set1, set2):
    """
    Return the difference of two sets.

    Parameters
    ----------
    set1 : set
        The set from which elements will be subtracted.
    set2 : set
        The set containing elements to subtract from set1.

    Returns
    -------
    set
        A new set containing elements that are in set1 but not in set2.

    Examples
    --------
    >>> find_set_difference({1, 2, 3}, {2, 4})
    {1, 3}
    """
    return set1.difference(set2)