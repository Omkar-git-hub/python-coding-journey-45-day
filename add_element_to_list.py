def add_element_to_list(lst, element):
    """
    Adds an element to the end of a list and returns the new list.

    Parameters
    ----------
    lst : list
        The original list to which the element will be added.
    element : Any
        The element to add to the list.

    Returns
    -------
    list
        A new list containing all elements of `lst` followed by `element`.

    Notes
    -----
    The original list is not modified; a shallow copy is created and returned.
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    new_list = lst.copy()
    new_list.append(element)
    return new_list

# End of file