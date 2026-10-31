def remove_dictionary_key(dictionary: dict, key) -> dict:
    """
    Remove a key from the given dictionary.

    If the key exists, it is removed; otherwise the dictionary is returned unchanged.
    The operation mutates the original dictionary and also returns it for convenience.

    Args:
        dictionary (dict): The dictionary from which to remove the key.
        key: The key to be removed.

    Returns:
        dict: The dictionary after the removal operation.
    """
    if key in dictionary:
        del dictionary[key]
    return dictionary


if __name__ == "__main__":
    # Example usage:
    # The user can input a dictionary literal and a key to remove.
    # Example:
    #   {"a": 1, "b": 2, "c": 3}
    #   b
    try:
        user_dict_input = input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): ").strip()
        user_key_input = input("Enter the key to remove: ").strip()
        # Safely evaluate the dictionary literal
        user_dict = eval(user_dict_input, {"__builtins__": {}})
        result = remove_dictionary_key(user_dict, user_key_input)
        print("Resulting dictionary:", result)
    except Exception as e:
        print("Error:", e)