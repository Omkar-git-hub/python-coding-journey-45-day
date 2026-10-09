def check_positive_or_negative(number: int) -> str:
    """
    Determine whether a given integer is positive, negative, or zero.

    Args:
        number (int): The integer to evaluate.

    Returns:
        str: "Positive" if number > 0,
             "Negative" if number < 0,
             "Zero" if number == 0.
    """
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


def _main() -> None:
    """
    Read an integer from standard input and print whether it is positive,
    negative, or zero.
    """
    try:
        user_input = input().strip()
        # Allow float inputs that represent whole numbers, but treat them as int
        if "." in user_input:
            number = int(float(user_input))
        else:
            number = int(user_input)
    except (ValueError, EOFError):
        # If input is invalid or missing, do nothing
        return

    result = check_positive_or_negative(number)
    print(result)


if __name__ == "__main__":
    _main()