def use_nested_if_statement(number):
    """
    Determines the nature of the input number using nested if statements.

    Parameters:
    number (int or float): The number to evaluate.

    Returns:
    str: A descriptive string indicating whether the number is positive even,
         positive odd, negative, or zero.
    """
    if number > 0:
        if number % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"