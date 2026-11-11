def update_nested_list_element(nested_list, row_index, col_index, new_value):
    """
    Updates an element in a nested list at the specified row and column index.
    
    Args:
        nested_list: The nested list to update.
        row_index: The index of the row (sublist).
        col_index: The index of the column (element within the sublist).
        new_value: The new value to assign.
        
    Returns:
        The updated nested list.
    """
    if 0 <= row_index < len(nested_list) and 0 <= col_index < len(nested_list[row_index]):
        nested_list[row_index][col_index] = new_value
    return nested_list

if __name__ == "__main__":
    # Example usage
    my_nested_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original nested list:")
    for row in my_nested_list:
        print(row)
    
    # Update element at row 1, column 1 (value 5) to 50
    updated_list = update_nested_list_element(my_nested_list, 1, 1, 50)
    
    print("\nUpdated nested list:")
    for row in updated_list:
        print(row)