def check_zero_or_non_zero(number):
    """
    Check if a number is zero or non-zero.
    
    Args:
        number: A numeric value to check
        
    Returns:
        str: "Zero" if the number is zero, "Non-Zero" otherwise
    """
    if number == 0:
        return "Zero"
    else:
        return "Non-Zero"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = check_zero_or_non_zero(num)
    print(f"{num} is {result}")