def find_set_union(set1, set2):
    """
    Return the union of two sets.

    Parameters:
    set1 (set): First set.
    set2 (set): Second set.

    Returns:
    set: A new set containing all unique elements from both input sets.
    """
    # Using the built‑in set union operation ensures the result is a new set.
    return set1.union(set2)