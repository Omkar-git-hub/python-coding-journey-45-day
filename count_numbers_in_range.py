def count_numbers_in_range(start, end):
    """
    Return the count of integers in the inclusive range [start, end].

    If start is greater than end, the function returns 0, indicating an empty range.

    Parameters
    ----------
    start : int
        The beginning of the range.
    end : int
        The end of the range.

    Returns
    -------
    int
        Number of integers from start to end inclusive.
    """
    if start > end:
        return 0
    return end - start + 1


if __name__ == "__main__":
    try:
        start_input = int(input())
        end_input = int(input())
        print(count_numbers_in_range(start_input, end_input))
    except Exception as e:
        # In case of invalid input, print nothing or an error message.
        # Keeping behavior consistent with other scripts: fail silently.
        pass