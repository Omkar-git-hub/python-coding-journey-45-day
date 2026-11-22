def create_text_file(filename, content):
    """
    Creates a text file with the given filename and content.
    
    Args:
        filename (str): The name of the file to create.
        content (str): The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    filename = "sample.txt"
    content = "Hello, World!\nThis is a sample text file."
    create_text_file(filename, content)
    print(f"File '{filename}' created successfully.")