def check_number_greater_than_10(number):
    """
    Determine whether the given number is greater than 10.

    Parameters
    ----------
    number : int or float
        The number to evaluate.

    Returns
    -------
    bool
        True if ``number`` is greater than 10, otherwise False.
    """
    return number > 10

if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        num = float(user_input) if "." in user_input else int(user_input)
        result = check_number_greater_than_10(num)
        print(f"The number {num} is {'greater' if result else 'not greater'} than 10.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")