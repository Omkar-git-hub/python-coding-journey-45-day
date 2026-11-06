def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate the compound interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): Annual interest rate (in percent).
    time (float): Time the money is invested for (in years).
    n (int, optional): Number of times that interest is compounded per year. Defaults to 1.

    Returns:
    float: The compound interest earned.
    """
    # Convert rate from percentage to decimal
    r_decimal = rate / 100.0
    # Compound amount
    amount = principal * (1 + r_decimal / n) ** (n * time)
    # Compound interest is the amount minus the principal
    return amount - principal


if __name__ == "__main__":
    try:
        principal_input = float(input().strip())
        rate_input = float(input().strip())
        time_input = float(input().strip())
        # Optional: number of times interest is compounded per year
        n_input = input().strip()
        n = int(n_input) if n_input else 1
    except Exception:
        # If inputs are not as expected, fall back to defaults
        principal_input = 0.0
        rate_input = 0.0
        time_input = 0.0
        n = 1

    result = calculate_compound_interest(principal_input, rate_input, time_input, n)
    # Print result rounded to 2 decimal places for consistency
    print(round(result, 2))