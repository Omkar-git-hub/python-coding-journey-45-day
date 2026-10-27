def find_symmetric_difference(set1, set2):
    """
    Return the symmetric difference of two sets.

    The symmetric difference contains elements that are in either of the
    input sets but not in both.

    Parameters
    ----------
    set1 : set
        First input set.
    set2 : set
        Second input set.

    Returns
    -------
    set
        A new set containing the symmetric difference of ``set1`` and ``set2``.
    """
    # Ensure the inputs are sets; if not, convert them to sets.
    set1 = set(set1) if not isinstance(set1, set) else set1
    set2 = set(set2) if not isinstance(set2, set) else set2

    # Use the built‑in symmetric_difference method for clarity and efficiency.
    return set1.symmetric_difference(set2)