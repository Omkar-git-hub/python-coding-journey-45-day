def count_digits(number: int) -> int:
    """
    Return the number of digits in an integer.

    Parameters
    ----------
    number : int
        The integer whose digits are to be counted.

    Returns
    -------
    int
        The count of digits in the absolute value of the input number.
    """
    return len(str(abs(number)))


if __name__ == "__main__":
    try:
        num = int(input().strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        print(count_digits(num))