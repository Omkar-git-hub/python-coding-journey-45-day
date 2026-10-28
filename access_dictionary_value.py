def access_dictionary_value(dictionary, key):
    """
    Access and return the value associated with a given key in a dictionary.
    
    Args:
        dictionary (dict): The dictionary to access.
        key: The key whose value is to be retrieved.
        
    Returns:
        The value associated with the key, or None if the key is not found.
    """
    return dictionary.get(key)


if __name__ == "__main__":
    # Example usage
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    # Access values
    name = access_dictionary_value(sample_dict, "name")
    age = access_dictionary_value(sample_dict, "age")
    city = access_dictionary_value(sample_dict, "city")
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
    # Access a non-existent key
    missing = access_dictionary_value(sample_dict, "email")
    print(f"Email: {missing}")