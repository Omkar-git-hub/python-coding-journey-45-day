def find_absolute_value(number):
    """
    Return the absolute value of a number.

    Parameters
    ----------
    number : int or float
        The number whose absolute value is to be computed.

    Returns
    -------
    int or float
        The absolute value of the input number.
    """
    return number if number >= 0 else -number

if __name__ == "__main__":
    # Simple manual tests
    assert find_absolute_value(5) == 5
    assert find_absolute_value(-3) == 3
    assert find_absolute_value(0) == 0
    assert find_absolute_value(-0.7) == 0.7
    print("All tests passed.")