def convert_tuple_to_list(input_tuple):
    """
    Convert a tuple to a list.

    Parameters:
    input_tuple (tuple): The tuple to be converted.

    Returns:
    list: A list containing the elements of the input tuple.
    """
    if not isinstance(input_tuple, tuple):
        raise TypeError("Input must be a tuple.")
    return list(input_tuple)