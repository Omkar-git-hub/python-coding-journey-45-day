def find_largest_of_three_numbers(a, b, c):
    """
    Find the largest of three numbers.
    
    Args:
        a: First number
        b: Second number
        c: Third number
        
    Returns:
        The largest of the three numbers
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    num1 = 10
    num2 = 20
    num3 = 15
    largest = find_largest_of_three_numbers(num1, num2, num3)
    print(f"The largest number is: {largest}")