def find_largest_element_in_list(lst):
    """
    Return the largest element in a list.

    Parameters
    ----------
    lst : list
        A list of comparable elements (e.g., numbers).

    Returns
    -------
    element
        The largest element in the list.

    Raises
    ------
    ValueError
        If the list is empty.

    Examples
    --------
    >>> find_largest_element_in_list([1, 5, 3, 9, 2])
    9
    >>> find_largest_element_in_list([-10, -5, -3])
    -3
    """
    if not lst:
        raise ValueError("The list is empty")

    largest = lst[0]
    for item in lst[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == "__main__":
    # Simple manual test
    sample = [3, 7, 2, 9, 5]
    print(f"Largest element in {sample} is {find_largest_element_in_list(sample)}")