def read_file_line_by_line(filename):
    """
    Reads a file line by line and prints each line.
    
    Args:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    # This assumes a file named 'sample.txt' exists in the current directory
    # If it doesn't exist, the error handling will catch it.
    read_file_line_by_line('sample.txt')