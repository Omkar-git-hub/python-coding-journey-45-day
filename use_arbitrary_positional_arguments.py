def use_arbitrary_positional_arguments(*args):
    """
    Accepts an arbitrary number of positional arguments and returns their sum.

    Parameters
    ----------
    *args : int or float
        Any number of numeric arguments.

    Returns
    -------
    int or float
        The sum of all provided arguments. If no arguments are provided, returns 0.

    Examples
    --------
    >>> use_arbitrary_positional_arguments(1, 2, 3)
    6
    >>> use_arbitrary_positional_arguments(5)
    5
    >>> use_arbitrary_positional_arguments()
    0
    """
    return sum(args)