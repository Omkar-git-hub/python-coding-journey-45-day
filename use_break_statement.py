def print_numbers_until_5():
    """
    Demonstrates the use of the break statement in a while loop.
    Prints numbers from 1 to 5 and then breaks out of the loop.
    """
    i = 1
    while True:
        print(i)
        i += 1
        if i > 5:
            break

def find_first_even_number():
    """
    Demonstrates the use of the break statement to exit a loop early
    when a condition is met. Finds and prints the first even number
    in a list.
    """
    numbers = [1, 3, 5, 8, 10, 12]
    for num in numbers:
        if num % 2 == 0:
            print(f"First even number found: {num}")
            break

def search_in_list():
    """
    Demonstrates using break to stop searching once an item is found.
    """
    items = ["apple", "banana", "cherry", "date"]
    target = "cherry"
    
    for item in items:
        if item == target:
            print(f"Found {target}!")
            break
    else:
        # This block executes only if the loop did not break
        print(f"{target} not found in the list.")

if __name__ == "__main__":
    print("Printing numbers 1 to 5 using break:")
    print_numbers_until_5()
    
    print("\nFinding first even number:")
    find_first_even_number()
    
    print("\nSearching for 'cherry' in list:")
    search_in_list()