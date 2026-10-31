def print_dictionary_values(dictionary):
    """
    Print all values from the given dictionary.

    Each value is printed on its own line in the order they appear
    when iterating over the dictionary's values.
    """
    for value in dictionary.values():
        print(value)


if __name__ == "__main__":
    # Example usage
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland"
    }
    print_dictionary_values(sample_dict)