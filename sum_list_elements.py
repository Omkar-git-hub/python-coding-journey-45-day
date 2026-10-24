def sum_list_elements(lst):
    """
    Return the sum of all numeric elements in the given list.

    Parameters
    ----------
    lst : list of int or float
        The list whose elements are to be summed.

    Returns
    -------
    int or float
        The sum of the elements.
    """
    return sum(lst)


if __name__ == "__main__":
    # Expect a space-separated list of numbers from standard input.
    try:
        numbers = list(map(float, input().split()))
        # If all numbers are integers, convert the result to int for cleaner output.
        total = sum_list_elements(numbers)
        if total.is_integer():
            total = int(total)
        print(total)
    except Exception as e:
        # In case of invalid input, print an error message.
        print(f"Error: {e}")