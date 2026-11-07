def find_string_index(string, substring):
    """
    Find the index of a substring within a string.
    
    Args:
        string (str): The main string to search in.
        substring (str): The substring to search for.
        
    Returns:
        int: The index of the first occurrence of the substring, or -1 if not found.
    """
    return string.find(substring)

if __name__ == "__main__":
    # Example usage
    text = "Hello, World!"
    search_term = "World"
    
    index = find_string_index(text, search_term)
    
    if index != -1:
        print(f"'{search_term}' found at index {index} in '{text}'")
    else:
        print(f"'{search_term}' not found in '{text}'")