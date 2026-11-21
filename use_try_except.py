def divide_numbers(a, b):
    """
    Divide two numbers using a try/except/finally block.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Returns
    -------
    float or None
        The division result if successful; otherwise None.

    The function prints messages for the result, any error, and a
    statement from the finally block.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    else:
        print(f"Result: {result}")
    finally:
        print("Finally block executed")
    return result