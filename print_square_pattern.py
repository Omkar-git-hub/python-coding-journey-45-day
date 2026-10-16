def print_square_pattern(size: int) -> None:
    """
    Prints a square pattern of asterisks (*) of the given size.

    Each line contains `size` asterisks without spaces.
    """
    for _ in range(size):
        print("*" * size)


def main() -> None:
    """
    Reads an integer from standard input and prints the square pattern.
    """
    try:
        user_input = input().strip()
        if not user_input:
            return
        size = int(user_input)
        if size < 0:
            # Negative sizes are not meaningful; do nothing.
            return
        print_square_pattern(size)
    except (ValueError, EOFError):
        # If input is not an integer or no input is provided, silently exit.
        return


if __name__ == "__main__":
    main()