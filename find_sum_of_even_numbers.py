def find_sum_of_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in a list.
    
    Args:
        numbers (list): A list of numbers.
        
    Returns:
        int: The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

if __name__ == "__main__":
    # Example usage
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_sum_of_even_numbers(sample_numbers)
    print(f"Sum of even numbers in {sample_numbers}: {result}")