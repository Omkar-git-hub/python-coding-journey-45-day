def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non‑negative integer.

    Args:
        n (int): The number to calculate the factorial for. Must be >= 0.

    Returns:
        int: The factorial of ``n``.

    Raises:
        ValueError: If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Simple manual test when run directly
    import sys

    try:
        number = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    print(f"Factorial of {number} is {calculate_factorial(number)}")