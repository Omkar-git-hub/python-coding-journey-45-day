def use_elif_statement(value):
    """
    Demonstrates the use of an elif statement.
    Returns a string indicating which condition was met.
    """
    if value < 0:
        return "negative"
    elif value == 0:
        return "zero"
    else:
        # Placeholder for future handling of positive values.
        pass
    return "positive"