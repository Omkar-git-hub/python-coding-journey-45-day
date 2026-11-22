def append_data_to_file(filename, data):
    """
    Appends data to a file.

    Args:
        filename (str): The name of the file to append to.
        data (str): The data to append.
    """
    with open(filename, 'a') as file:
        file.write(data)

if __name__ == "__main__":
    filename = "example_append.txt"
    data_to_append = "This is a line of data appended to the file.\n"
    
    append_data_to_file(filename, data_to_append)
    print(f"Data appended to {filename}")