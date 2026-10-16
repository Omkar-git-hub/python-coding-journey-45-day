def check_palindrome_string(s):
    """
    Check if a given string is a palindrome.
    
    Args:
        s (str): The string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_strings = [
        "racecar",
        "hello",
        "A man, a plan, a canal: Panama",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon"
    ]
    
    for test_str in test_strings:
        is_palindrome = check_palindrome_string(test_str)
        print(f"'{test_str}' is {'a' if is_palindrome else 'not a'} palindrome")