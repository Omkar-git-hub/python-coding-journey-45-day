def print_number_pattern():
    """
    Prints a numeric pattern using loops.

    The pattern prints numbers starting from 1 up to the current row number.
    Example for rows = 5:
    1
    12
    123
    1234
    12345
    """
    try:
        rows = int(input().strip())
    except Exception:
        # If input is not provided or invalid, default to 5 rows
        rows = 5

    for i in range(1, rows + 1):
        # Generate numbers from 1 to i and join them without spaces
        line = ''.join(str(num) for num in range(1, i + 1))
        print(line)


if __name__ == "__main__":
    print_number_pattern()