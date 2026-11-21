def use_any_all_functions(numbers):
    """
    Demonstrates the use of Python's built-in any() and all() functions.

    Parameters
    ----------
    numbers : list[int]
        A list of integers to evaluate.

    Returns
    -------
    tuple[bool, bool]
        A tuple where the first element is True if any number in the list is even,
        and the second element is True if all numbers in the list are even.
    """
    any_even = any(num % 2 == 0 for num in