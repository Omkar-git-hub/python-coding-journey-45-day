def remove_element_from_list(lst, element):
    """
    Return a new list with all occurrences of `element` removed from `lst`.

    Parameters
    ----------
    lst : list
        The original list.
    element : Any
        The element to be removed.

    Returns
    -------
    list
        A new list without the specified element.

    Examples
    --------
    >>> remove_element_from_list([1, 2, 3, 2], 2)
    [1, 3]
    >>> remove_element_from_list(['a', 'b', 'c'], 'd')
    ['a', 'b', 'c']
    """
    return [item for item in lst if item != element]


if __name__ == "__main__":
    # Simple interactive demo
    import ast
    import sys

    if len(sys.argv) != 3:
        print("Usage: python remove_element_from_list.py <list> <element>")
        print("Example: python remove_element_from_list.py \"[1,2,3,2]\" 2")
        sys.exit(1)

    input_list = ast.literal_eval(sys.argv[1])
    element_to_remove = ast.literal_eval(sys.argv[2])
    result = remove_element_from_list(input_list, element_to_remove)
    print(result)