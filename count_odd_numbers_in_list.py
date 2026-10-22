def count_odd_numbers_in_list(numbers):
    """
    Count the odd numbers in a list.

    Parameters
    ----------
    numbers : list[int] or iterable of int
        The list (or any iterable) containing integer numbers.

    Returns
    -------
    int
        The count of numbers that are odd.

    Examples
    --------
    >>> count_odd_numbers_in_list([1, 2, 3, 4, 5])
    3
    """
    return sum(1 for num in numbers if isinstance(num, int) and num % 2 != 0)


if __name__ == "__main__":
    # Simple demonstration when run directly.
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The list: {sample_list}")
    print(f"Number of odd elements: {count_odd_numbers_in_list(sample_list)}")