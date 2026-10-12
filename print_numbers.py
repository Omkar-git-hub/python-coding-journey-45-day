"""
Print Numbers From 1 to 10

This script prints the integers from 1 to 10 inclusive,
each on a separate line. It follows the style of the
existing print_* modules in the repository.
"""

def print_numbers() -> None:
    """
    Iterate over the range 1 to 10 and print each number.
    """
    for number in range(1, 11):
        print(number)

if __name__ == "__main__":
    print_numbers()