def create_set(iterable):
    """
    Create a set from the given iterable, removing duplicate elements.

    Parameters
    ----------
    iterable : iterable
        Any iterable (list, tuple, string, etc.) from which to build the set.

    Returns
    -------
    set
        A set containing the unique elements from the iterable.
    """
    return set(iterable)


if __name__ == "__main__":
    import sys
    import ast

    # If command‑line arguments are provided, treat them as the data source.
    if len(sys.argv) > 1:
        # Join arguments and try to evaluate as a Python literal (e.g., "[1, 2, 2]")
        try:
            data = ast.literal_eval(" ".join(sys.argv[1:]))
        except Exception:
            # Fallback: treat each argument as a separate element
            data = sys.argv[1:]
        result_set = create_set(data)
    else:
        # No arguments: read from standard input.
        input_data = sys.stdin.read().strip()
        if input_data:
            try:
                data = ast.literal_eval(input_data)
            except Exception:
                # Assume space‑separated values if not a valid literal
                data = input_data.split()
            result_set = create_set(data)
        else:
            result_set = set()

    print(result_set)