def find_remainder(dividend: int, divisor: int) -> int:
    """
    Calculate the remainder of dividing ``dividend`` by ``divisor``.

    Parameters
    ----------
    dividend : int
        The number to be divided.
    divisor : int
        The number by which ``dividend`` is divided.

    Returns
    -------
    int
        The remainder after integer division.

    Raises
    ------
    ZeroDivisionError
        If ``divisor`` is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    return dividend % divisor


if __name__ == "__main__":
    import sys

    # Expect two integers provided via standard input, separated by whitespace.
    # Example usage: echo "10 3" | python find_remainder.py
    try:
        data = sys.stdin.read().strip().split()
        if len(data) != 2:
            raise ValueError("Exactly two integers are required as input.")
        a, b = map(int, data)
        result = find_remainder(a, b)
        print(result)
    except Exception as e:
        print(f"Error: {e}")