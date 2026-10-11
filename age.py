def print_age(age: int) -> None:
    """
    Print whether the given age corresponds to an adult or a minor.

    An adult is defined as a person whose age is 18 years or older.
    A minor is anyone younger than 18.

    Parameters
    ----------
    age : int
        The age to evaluate.

    Returns
    -------
    None
        The function prints "Adult" if age >= 18, otherwise prints "Minor".
    """
    if age >= 18:
        print("Adult")
    else:
        print("Minor")