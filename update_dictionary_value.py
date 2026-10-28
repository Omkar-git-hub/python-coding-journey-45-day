def update_dictionary_value(dictionary, key, new_value):
    """
    Update the value associated with `key` in the given `dictionary`.

    If the key does not exist, it will be added to the dictionary.
    The function returns the updated dictionary.

    Parameters
    ----------
    dictionary : dict
        The dictionary to be updated.
    key : hashable
        The key whose value should be updated.
    new_value : any
        The new value to associate with the key.

    Returns
    -------
    dict
        The updated dictionary.
    """
    dictionary[key] = new_value
    return dictionary


if __name__ == "__main__":
    # Simple interactive demonstration.
    # Expected input:
    #   First line: a dictionary literal (e.g., {"a": 1, "b": 2})
    #   Second line: the key to update/add
    #   Third line: the new value (attempts to convert to int if possible)
    import ast

    try:
        raw_dict = input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): ").strip()
        user_dict = ast.literal_eval(raw_dict)
        if not isinstance(user_dict, dict):
            raise ValueError
    except Exception:
        print("Invalid dictionary input.")
        exit(1)

    key = input("Enter the key to update/add: ").strip()
    value_input = input("Enter the new value: ").strip()

    # Try to interpret the value as an integer, float, or keep as string
    try:
        new_value = int(value_input)
    except ValueError:
        try:
            new_value = float(value_input)
        except ValueError:
            new_value = value_input

    updated_dict = update_dictionary_value(user_dict, key, new_value)
    print("Updated dictionary:", updated_dict)