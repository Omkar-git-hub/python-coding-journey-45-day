def count_tuple_occurrences(tuples_list, target_tuple):
    """
    Count how many times `target_tuple` appears in `tuples_list`.

    Parameters
    ----------
    tuples_list : list of tuple
        The list in which to search for the target tuple.
    target_tuple : tuple
        The tuple whose occurrences need to be counted.

    Returns
    -------
    int
        The number of occurrences of `target_tuple` in `tuples_list`.
    """
    if not isinstance(tuples_list, list):
        raise TypeError("First argument must be a list of tuples.")
    if not isinstance(target_tuple, tuple):
        raise TypeError("Second argument must be a tuple.")

    return sum(1 for item in tuples_list if item == target_tuple)


if __name__ == "__main__":
    # Example usage
    sample_list = [(1, 2), (3, 4), (1, 2), (5, 6), (1, 2)]
    target = (1, 2)
    print(f"The tuple {target} appears {count_tuple_occurrences(sample_list, target)} times.")