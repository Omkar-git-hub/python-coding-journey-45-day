def get_dictionary_with_default(dictionary, key, default_value):
    """
    Retrieve the value for *key* from *dictionary*.
    If the key is not present, return *default_value* instead.

    Parameters
    ----------
    dictionary : dict
        The dictionary to search.
    key : hashable
        The key whose value is to be retrieved.
    default_value : any
        The value to return if *key* is not found in the dictionary.

    Returns
    -------
    any
        The value associated with *key* if it exists, otherwise *default_value*.
    """
    return dictionary.get(key, default_value)