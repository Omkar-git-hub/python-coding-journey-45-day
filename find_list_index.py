def find_list_index(lst, element):
    """
    Find the index of an element in a list.
    
    Args:
        lst: The list to search in.
        element: The element to find.
        
    Returns:
        The index of the element if found, otherwise -1.
    """
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

if __name__ == "__main__":
    # Example usage
    sample_list = [10, 20, 30, 40, 50]
    
    # Test finding an existing element
    element_to_find = 30
    index = find_list_index(sample_list, element_to_find)
    if index != -1:
        print(f"Element {element_to_find} found at index {index}")
    else:
        print(f"Element {element_to_find} not found in the list")
    
    # Test finding a non-existing element
    element_to_find = 60
    index = find_list_index(sample_list, element_to_find)
    if index != -1:
        print(f"Element {element_to_find} found at index {index}")
    else:
        print(f"Element {element_to_find} not found in the list")