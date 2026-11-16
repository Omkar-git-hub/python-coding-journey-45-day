def print_kwargs(**kwargs):
    """
    Print each keyword argument on a separate line in the format 'key: value'.

    This function demonstrates the use of arbitrary keyword arguments (**kwargs).
    It iterates over the provided keyword arguments and prints them.

    Example:
        print_kwargs(name="Alice", age=30)
        # Output:
        # name: Alice
        # age: 30
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def get_kwargs_as_dict(**kwargs):
    """
    Return the keyword arguments as a dictionary.

    This utility function can be used when you need to work with the
    collected keyword arguments programmatically.

    Example:
        result = get_kwargs_as_dict(city="Paris", country="France")
        # result -> {'city': 'Paris', 'country': 'France'}
    """
    return dict(kwargs)