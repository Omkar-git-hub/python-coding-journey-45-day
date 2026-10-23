def reverse_list(lst: list) -> list:
    """
    Return a new list containing the elements of *lst* in reverse order.

    The original list is not modified.

    Parameters
    ----------
    lst : list
        The list to be reversed.

    Returns
    -------
    list
        A new list with the elements reversed.
    """
    return lst[::-1]


if __name__ == "__main__":
    # Expect a Python list literal as input, e.g., [1, 2, 3]
    try:
        input_list = eval(input().strip())
        if not isinstance(input_list, list):
            raise ValueError
    except Exception:
        # Fallback: treat the input as space‑separated values
        input_list = input().strip().split()
    print(reverse_list(input_list))