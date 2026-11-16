def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def square_number(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

def max_of_two(a, b):
    return a if a > b else b

def main():
    # Define lambda functions
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    square = lambda x: x ** 2
    check_even = lambda x: x % 2 == 0
    find_max = lambda x, y: x if x > y else y

    # Test the lambda functions
    print(f"Addition: {add(5, 3)}")
    print(f"Multiplication: {multiply(4, 6)}")
    print(f"Square of 7: {square(7)}")
    print(f"Is 10 even? {check_even(10)}")
    print(f"Is 7 even? {check_even(7)}")
    print(f"Max of 15 and 20: {find_max(15, 20)}")
    print(f"Max of 25 and 10: {find_max(25, 10)}")

    # Demonstrate lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"Squared numbers: {squared_numbers}")

    # Demonstrate lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")

    # Demonstrate lambda with sorted
    words = ["banana", "apple", "cherry", "date"]
    sorted_by_length = sorted(words, key=lambda word: len(word))
    print(f"Words sorted by length: {sorted_by_length}")

if __name__ == "__main__":
    main()