def check_set_membership(element, sample_set):
    """
    Check if an element is present in a given set.

    Args:
        element: The element to check for.
        sample_set: The set to search in.

    Returns:
        True if the element is in the set, False otherwise.
    """
    return element in sample_set

if __name__ == "__main__":
    # Example usage
    my_set = {1, 2, 3, 4, 5}
    
    # Test cases
    print(check_set_membership(3, my_set))  # True
    print(check_set_membership(6, my_set))  # False