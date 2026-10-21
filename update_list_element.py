def update_list_element(lst, index, new_value):
    """
    Update the element at the specified index in the list with a new value.

    Parameters
    ----------
    lst : list
        The list to be updated.
    index : int
        The position of the element to replace. Supports negative indexing
        as per standard Python list behavior.
    new_value : Any
        The new value to set at the given index.

    Returns
    -------
    list
        The list after the update. The original list is modified in place
        and also returned for convenience.

    Raises
    ------
    TypeError
        If ``lst`` is not a list.
    IndexError
        If ``index`` is out of range for the list.
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    # This will naturally raise IndexError if out of bounds
    lst[index] = new_value
    return lst