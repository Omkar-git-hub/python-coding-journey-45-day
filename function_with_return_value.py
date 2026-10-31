def get_greeting(name: str) -> str:
    """
    Return a greeting message for the provided name.

    Parameters
    ----------
    name : str
        The name to greet.

    Returns
    -------
    str
        A greeting string in the form "Hello, {name}!".
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Example usage: print a greeting for the user "World"
    print(get_greeting("World"))