"""
add_dictionary_key.py

This module provides a utility function to add a key-value pair to an existing dictionary.
The function returns a new dictionary with the added key, leaving the original dictionary unchanged.
"""

from typing import Dict, Any


def add_dictionary_key(dictionary: Dict[Any, Any], key: Any, value: Any) -> Dict[Any, Any]:
    """
    Return a new dictionary that contains all items from the original dictionary
    plus the specified key-value pair. If the key already exists, its value is
    overwritten.

    Parameters
    ----------
    dictionary : dict
        The original dictionary to which the key-value pair will be added.
    key : Any
        The key to add to the dictionary.
    value : Any
        The value associated with the key.

    Returns
    -------
    dict
        A new dictionary containing the original items and the new key-value pair.
    """
    # Create a shallow copy to avoid mutating the original dictionary
    new_dict = dictionary.copy()
    new_dict[key] = value
    return new_dict


if __name__ == "__main__":
    # Example usage
    sample_dict = {"name": "Alice", "age": 30}
    updated_dict = add_dictionary_key(sample_dict, "city", "New York")
    print(f"Original dictionary: {sample_dict}")
    print(f"Updated dictionary: {updated_dict}")