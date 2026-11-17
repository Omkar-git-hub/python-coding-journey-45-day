def zip_lists(list1, list2):
    """
    Pair elements from two lists using the built‑in ``zip`` function.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A list of tuples where each tuple contains one element from
              ``list1`` and the corresponding element from ``list2``.
              If the lists are of unequal length, pairing stops at the
              shorter list, mirroring the behaviour of ``zip``.
    """
    return list(zip(list1, list2))


def unzip_lists(paired):
    """
    Separate a list of paired tuples back into two individual lists.

    Args:
        paired (list[tuple]): A list where each item is a tuple containing
                              two elements.

    Returns:
        tuple: A tuple containing two lists. The first list holds all the
               first elements of the input tuples, and the second list holds
               all the second elements. If ``paired`` is empty, two empty
               lists are returned.
    """
    if not paired:
        return [], []
    first, second = zip(*paired)
    return list(first), list(second)