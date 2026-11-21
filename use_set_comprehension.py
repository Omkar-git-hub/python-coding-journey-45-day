def get_even_squares(numbers):
    """
    Return a set containing the squares of all even numbers in the provided iterable.

    Parameters
    ----------
    numbers : iterable of int
        An iterable containing integer values.

    Returns
    -------
    set[int]
        A set of squares of the even numbers found in ``numbers``.
    """
    return {num * num for num in numbers if num % 2 == 0}