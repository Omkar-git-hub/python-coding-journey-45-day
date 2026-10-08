"""
Utility module for checking the type of a variable.

Provides a simple function that returns the name of the type of the given
value as a string. This is useful for educational exercises where the
focus is on understanding Python's built‑in types.
"""

def check_variable_type(value):
    """
    Return the name of the type of *value*.

    Parameters
    ----------
    value : Any
        The value whose type is to be inspected.

    Returns
    -------
    str
        The name of the type (e.g., ``'int'``, ``'float'``, ``'bool'``,
        ``'str'``, etc.).
    """
    return type(value).__name__