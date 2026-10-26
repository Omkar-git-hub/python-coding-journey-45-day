def remove_duplicate_elements(input_list):
    """
    Remove duplicate elements from the given list using a set.

    Parameters
    ----------
    input_list : list
        The list from which duplicate elements should be removed.

    Returns
    -------
    list
        A new list containing the unique elements from ``input_list``.
        The order of elements is not guaranteed because a set is used.
    """
    # Convert the list to a set to eliminate duplicates, then back to a list.
    return list(set(input_list))


if __name__ == "__main__":
    # Simple interactive demonstration
    try:
        raw_input = input("Enter list elements separated by spaces: ")
        # Attempt to interpret numbers; otherwise keep as strings
        elements = [
            int(item) if item.lstrip("-").isdigit() else item
            for item in raw_input.split()
        ]
        result = remove_duplicate_elements(elements)
        print("List after removing duplicates:", result)
    except Exception as e:
        print(f"Error: {e}")