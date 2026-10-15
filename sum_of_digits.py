def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of the digits of an integer.

    Args:
        number (int): The integer whose digits will be summed. Can be negative.

    Returns:
        int: Sum of the absolute value's digits.
    """
    # Work with absolute value to handle negative numbers
    number = abs(number)
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    try:
        user_input = input("Enter an integer: ").strip()
        num = int(user_input)
        print(sum_of_digits(num))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")