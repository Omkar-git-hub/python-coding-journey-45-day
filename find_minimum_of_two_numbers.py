def find_minimum_of_two_numbers(a, b):
    """
    Return the smaller of two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.

    Returns
    -------
    int or float
        The minimum of ``a`` and ``b``.
    """
    return a if a < b else b


if __name__ == "__main__":
    # Read two numbers from standard input, one per line.
    try:
        first = float(input())
        second = float(input())
        minimum = find_minimum_of_two_numbers(first, second)

        # Print as integer if the result is an integer value.
        if isinstance(minimum, float) and minimum.is_integer():
            print(int(minimum))
        else:
            print(minimum)
    except Exception:
        # If input is not as expected, fail silently (consistent with other scripts).
        pass