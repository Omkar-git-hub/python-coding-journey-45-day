def check_even_or_odd(number: int) -> str:
    """
    Determine whether an integer is even or odd.

    Parameters
    ----------
    number : int
        The integer to evaluate.

    Returns
    -------
    str
        "Even" if the number is divisible by 2, otherwise "Odd".
    """
    return "Even" if number % 2 == 0 else "Odd"