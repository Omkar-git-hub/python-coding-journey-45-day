def get_nested_element(nested_list, indices):
    """
    Retrieve an element from a nested list using a sequence of indices.

    Parameters
    ----------
    nested_list : list
        The list that may contain other lists (nested arbitrarily).
    indices : iterable of int
        A sequence of indices that navigate through the nested lists.

    Returns
    -------
    Any
        The element located at the specified path.

    Raises
    ------
    IndexError
        If any index is out of range for its corresponding sub‑list.
    TypeError
        If an intermediate element is not a list when more indices remain.
    """
    element = nested_list
    for idx in indices:
        if not isinstance(element, list):
            raise TypeError(
                f"Expected a list at this level, but got {type(element).__name__}"
            )
        element = element[idx]
    return element


# Example usage (executed when the module is run directly)
if __name__ == "__main__":
    # A sample nested list
    sample_nested = [
        [1, 2, [10, 20]],
        [3, 4, [30, 40]],
        [5, 6, [50, 60]],
    ]

    # Access the element '20' which is at path [0, 2, 1]
    result = get_nested_element(sample_nested, [0, 2, 1])
    print(f"The accessed element is: {result}")