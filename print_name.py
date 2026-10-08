def print_name():
    """
    Reads a name from standard input and prints it.
    """
    try:
        name = input()
    except EOFError:
        name = ""
    print(name)


if __name__ == "__main__":
    print_name()