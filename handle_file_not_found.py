import os


def read_file_content(file_path):
    """
    Reads and returns the content of a file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    with open(file_path, 'r') as file:
        return file.read()


def safe_read_file(file_path):
    """
    Safely reads a file, handling FileNotFoundError.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file if it exists, otherwise an error message.
    """
    try:
        return read_file_content(file_path)
    except FileNotFoundError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # Example usage
    print(safe_read_file("non_existent_file.txt"))
    print(safe_read_file("README.md"))