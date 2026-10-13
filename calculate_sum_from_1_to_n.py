def calculate_sum_from_1_to_n(n):
    """
    Calculate the sum of all integers from 1 to n.
    
    Args:
        n (int): The upper limit of the range (inclusive).
        
    Returns:
        int: The sum of integers from 1 to n.
    """
    if n < 1:
        return 0
    return n * (n + 1) // 2

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = calculate_sum_from_1_to_n(n)
    print(f"Sum from 1 to {n} is: {result}")