def find_quotient(a, b):
    """
    Returns the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Division by zero is not allowed") from e