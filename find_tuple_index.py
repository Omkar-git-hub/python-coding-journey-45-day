<code>
def find_tuple_index(tuple_obj, element):
    """
    Find the index of an element in a tuple.

    Parameters
    ----------
    tuple_obj : tuple
        The tuple to search.
    element : Any
        The element to find within the tuple.

    Returns
    -------
    int
        The index of the element if found; otherwise, -1.
    """
    try:
        return tuple_obj.index(element)
    except ValueError:
        return -1


if __name__ == "__main__":
    sample_tuple = (10, 20, 30, 40, 50)
    print(f"Index of 30: {find_tuple_index(sample_tuple, 30)}")  # Expected: 2
    print(f"Index of 60: {find_tuple_index(sample_tuple, 60)}")  # Expected: -1
</code>