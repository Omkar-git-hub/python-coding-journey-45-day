def copy_list(original_list):
    """
    Return a shallow copy of the given list.

    Parameters:
        original_list (list): The list to be copied.

    Returns:
        list: A new list containing the same elements as original_list.
    """
    # Using the list's built‑in copy method provides a shallow copy.
    return original_list.copy()


if __name__ == "__main__":
    # Example usage
    sample = [1, 2, 3, 4]
    copied = copy_list(sample)
    print("Original list:", sample)
    print("Copied list:", copied)