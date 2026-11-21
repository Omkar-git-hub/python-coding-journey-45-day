def main():
    """
    Demonstrates the use of multiple except blocks to handle different
    types of exceptions that may arise during user input and arithmetic
    operations.

    The function prompts the user for two numbers, attempts to convert
    them to integers, and then divides the first number by the second.
    Specific exceptions are caught and handled with informative messages.
    """
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError as ve:
        # Handles cases where the input cannot be converted to an int.
        print(f"Input error: {ve}. Please enter valid integers.")
    except ZeroDivisionError as zde:
        # Handles division by zero.
        print(f"Math error: {zde}. The second number cannot be zero.")
    except Exception as e:
        # Catches any other unforeseen exceptions.
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()