"""Module to create and manage an integer variable."""

# Create an integer variable
integer_variable = 42


def get_integer_variable() -> int:
    """Return the current value of the integer variable.

    Returns:
        int: The value of the integer variable.
    """
    return integer_variable


def set_integer_variable(value: int) -> None:
    """Set the value of the integer variable.

    Args:
        value (int): The new value for the integer variable.

    Raises:
        TypeError: If the provided value is not an integer.
    """
    global integer_variable
    if not isinstance(value, int):
        raise TypeError("Value must be an integer")
    integer_variable = value