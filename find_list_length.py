def find_list_length(lst):
    """
    Find the length of a list.
    
    Args:
        lst: The list to find the length of.
        
    Returns:
        int: The length of the list.
    """
    return len(lst)

if __name__ == "__main__":
    # Example usage
    sample_list = [1, 2, 3, 4, 5]
    length = find_list_length(sample_list)
    print(f"List: {sample_list}")
    print(f"Length: {length}")