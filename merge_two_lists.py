def merge_two_lists(list1, list2):
    """
    Merges two lists into a single list.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        
    Returns:
        list: A new list containing all elements from list1 followed by all elements from list2.
    """
    return list1 + list2

if __name__ == "__main__":
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    merged = merge_two_lists(list_a, list_b)
    print(f"List 1: {list_a}")
    print(f"List 2: {list_b}")
    print(f"Merged List: {merged}")