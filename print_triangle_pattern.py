def print_triangle_pattern(n):
    """Print a triangle pattern of asterisks with n rows."""
    for i in range(1, n + 1):
        print("*" * i)


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    print_triangle_pattern(n)