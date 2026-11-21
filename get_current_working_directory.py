import os

def get_current_working_directory() -> str:
    """
    Returns the absolute path of the current working directory.

    Returns:
        str: The current working directory path.
    """
    return os.getcwd()

if __name__ == "__main__":
    print(get_current_working_directory())