def check_dictionary_key(dictionary, key):
    """
    Check if a key exists in a dictionary.

    Args:
        dictionary (dict): The dictionary to check.
        key: The key to look for.

    Returns:
        bool: True if the key exists in the dictionary, False otherwise.
    """
    return key in dictionary

if __name__ == "__main__":
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    key_to_check = "name"
    if check_dictionary_key(sample_dict, key_to_check):
        print(f"Key '{key_to_check}' exists in the dictionary.")
    else:
        print(f"Key '{key_to_check}' does not exist in the dictionary.")
        
    key_to_check = "email"
    if check_dictionary_key(sample_dict, key_to_check):
        print(f"Key '{key_to_check}' exists in the dictionary.")
    else:
        print(f"Key '{key_to_check}' does not exist in the dictionary.")