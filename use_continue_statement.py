def use_continue_statement():
    """
    Demonstrates the use of the `continue` statement in a for loop.
    Prints all odd numbers from 1 to 10 inclusive.
    """
    for number in range(1, 11):
        if number % 2 == 0:
            continue
        print(number)

if __name__ == "__main__":
    use_continue_statement()