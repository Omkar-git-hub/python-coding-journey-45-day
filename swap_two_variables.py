def swap_two_variables(a, b):
    """
    Swap two variables and return them in swapped order.

    Parameters:
    a: First variable.
    b: Second variable.

    Returns:
    tuple: (b, a) where the values are swapped.
    """
    return b, a


if __name__ == "__main__":
    # Read two inputs from the user. Attempt to convert them to integers,
    # but if conversion fails, keep them as strings.
    a_input = input()
    b_input = input()
    try:
        a = int(a_input)
    except ValueError:
        a = a_input
    try:
        b = int(b_input)
    except ValueError:
        b = b_input

    swapped_a, swapped_b = swap_two_variables(a, b)
    # Print the swapped values separated by a space.
    print(swapped_a, swapped_b)