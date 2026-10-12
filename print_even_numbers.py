def print_even_numbers(start, end):
    """
    Prints all even numbers in the range from start to end (inclusive).
    
    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
    """
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

if __name__ == "__main__":
    # Example usage
    print_even_numbers(1, 10)