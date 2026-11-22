def main():
    """
    Demonstrates the use of a try/except block with an else clause.
    The else clause is executed only if no exception occurs in the try block.
    """
    try:
        # Prompt the user for a number and attempt to convert it to an integer.
        num = int(input("Enter a number: "))
    except ValueError:
        # Handle the case where the input cannot be converted to an integer.
        print("Invalid input, please enter a valid integer.")
    else:
        # This block runs only if the try block succeeded without raising an exception.
        print(f"You entered the number: {num}")


if __name__ == "__main__":
    main()