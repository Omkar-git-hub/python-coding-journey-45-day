def check_palindrome_number(number):
    """
    Check if a given number is a palindrome.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    if number < 0:
        return False
    
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if check_palindrome_number(num):
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")