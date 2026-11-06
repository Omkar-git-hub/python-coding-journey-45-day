def find_ascii_value(char):
    """
    Find the ASCII value of a given character.
    
    Args:
        char (str): A single character string.
        
    Returns:
        int: The ASCII value of the character.
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return ord(char)

if __name__ == "__main__":
    # Example usage
    test_char = 'A'
    ascii_value = find_ascii_value(test_char)
    print(f"The ASCII value of '{test_char}' is {ascii_value}")