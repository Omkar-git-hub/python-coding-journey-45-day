def print_odd_numbers():
    """
    Prints all odd numbers from 1 to 10 inclusive.
    """
    for number in range(1, 11):
        if number % 2 != 0:
            print(number)

if __name__ == "__main__":
    print_odd_numbers()