def flatten_list(lst):
    """
    Flatten a simple list of lists into a single list.

    Parameters
    ----------
    lst : list
        A list containing sublists (e.g., [[1, 2], [3, 4], [5]]).

    Returns
    -------
    list
        A single flattened list containing all elements from the sublists in order.
    """
    # Using a list comprehension to iterate over each sublist and then over each element within that sublist.
    return [item for sublist in lst for item in sublist]