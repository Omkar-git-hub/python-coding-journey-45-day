def find_quotient(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend // divisor