def sort_list(lst):
    """
    Sorts a list in ascending order.
    
    Args:
        lst: The list to sort.
        
    Returns:
        A new sorted list.
    """
    return sorted(lst)

if __name__ == "__main__":
    # Example usage
    sample_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sort_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Sorted list: {sorted_list}")