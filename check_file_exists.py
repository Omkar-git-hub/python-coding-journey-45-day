import os

def check_file_exists(filename):
    """
    Check if a file exists in the current directory.
    
    Args:
        filename (str): The name of the file to check.
        
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filename)

if __name__ == "__main__":
    # Example usage
    test_file = "test_file.txt"
    
    # Create a temporary file for demonstration
    with open(test_file, 'w') as f:
        f.write("This is a test file.")
    
    if check_file_exists(test_file):
        print(f"'{test_file}' exists.")
    else:
        print(f"'{test_file}' does not exist.")
    
    # Check for a non-existent file
    non_existent_file = "non_existent_file.txt"
    if check_file_exists(non_existent_file):
        print(f"'{non_existent_file}' exists.")
    else:
        print(f"'{non_existent_file}' does not exist.")
    
    # Clean up the test file
    os.remove(test_file)