def find_element_frequency(lst, element):
    """
    Returns the frequency of `element` in the list `lst`.

    Parameters
    ----------
    lst : list
        The list in which to count occurrences.
    element : Any
        The element whose frequency is to be counted.

    Returns
    -------
    int
        Number of times `element` appears in `lst`.
    """
    return lst.count(element)


if __name__ == "__main__":
    # Expect the first line to be space‑separated values for the list.
    # The second line contains the element to search for.
    try:
        raw_list = input().strip()
        # If the input looks like a Python list literal, evaluate it.
        if raw_list.startswith('[') and raw_list.endswith(']'):
            import ast
            lst = ast.literal_eval(raw_list)
        else:
            # Default to a list of strings split by whitespace.
            lst = raw_list.split()
        element_input = input().strip()
        # Try to interpret the element as an integer or float if possible.
        try:
            element = int(element_input)
        except ValueError:
            try:
                element = float(element_input)
            except ValueError:
                element = element_input
        print(find_element_frequency(lst, element))
    except EOFError:
        # No input provided; nothing to do.
        pass