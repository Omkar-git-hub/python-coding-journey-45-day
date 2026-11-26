def count_words(file_path):
    """
    Count the number of words in the given file.

    A word is defined as any sequence of characters separated by whitespace.
    If the file does not exist, the function returns 0.

    Parameters
    ----------
    file_path : str
        Path to the file to be read.

    Returns
    -------
    int
        The total number of words in the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # split on any whitespace to get words
        words = content.split()
        return len(words)
    except FileNotFoundError:
        # Consistent with other utilities in the repo that treat missing files as empty
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python count_words.py <file_path>")
    else:
        path = sys.argv[1]
        print(count_words(path))