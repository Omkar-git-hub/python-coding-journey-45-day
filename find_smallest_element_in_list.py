def find_smallest_element_in_list(lst):
    """
    Return the smallest element in the given list.

    Parameters
    ----------
    lst : list
        A list of comparable elements.

    Returns
    -------
    The smallest element in the list, or None if the list is empty.
    """
    if not lst:
        return None

    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item
    return smallest


if __name__ == "__main__":
    # Example usage: user provides space‑separated values.
    try:
        user_input = input("Enter list elements separated by space: ").strip()
        # Attempt to convert to integers; fall back to strings if conversion fails.
        elements = [int(x) for x in user_input.split()] if user_input else []
    except ValueError:
        # If conversion to int fails, treat elements as strings.
        elements = user_input.split() if user_input else []

    result = find_smallest_element_in_list(elements)
    print(result)