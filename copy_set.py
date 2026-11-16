def copy_set(original_set):
    """
    Return a shallow copy of the given set.

    Parameters:
        original_set (set): The set to be copied.

    Returns:
        set: A new set containing the same elements as original_set.
    """
    return original_set.copy()


if __name__ == "__main__":
    # Example usage
    original = {1, 2, 3, 4}
    copied = copy_set(original)
    print("Original set:", original)
    print("Copied set:", copied)