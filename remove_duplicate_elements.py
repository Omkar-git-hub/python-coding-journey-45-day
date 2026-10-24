def remove_duplicate_elements(lst):
    """
    Remove duplicate elements from a list while preserving the original order.

    Parameters
    ----------
    lst : list
        The list from which duplicates should be removed.

    Returns
    -------
    list
        A new list containing the elements of ``lst`` without duplicates,
        preserving their first occurrence order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    # Simple interactive demo:
    # Input a space‑separated list of values (e.g., "1 2 3 2 4").
    try:
        raw_input = input("Enter list elements separated by spaces: ").strip()
        # Attempt to convert to integers; fall back to strings if conversion fails.
        elements = []
        for token in raw_input.split():
            try:
                elements.append(int(token))
            except ValueError:
                elements.append(token)
        print(remove_duplicate_elements(elements))
    except EOFError:
        # No input provided; do nothing.
        pass