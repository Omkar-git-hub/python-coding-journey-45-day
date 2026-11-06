"""
calculate_simple_interest.py

This module provides a function to calculate simple interest based on the
principal amount, annual interest rate, and time period in years.

Simple Interest Formula:
    SI = (Principal * Rate * Time) / 100

The function returns the calculated simple interest as a float.
"""

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate the simple interest.

    Parameters
    ----------
    principal : float
        The principal amount (initial investment or loan amount).
    rate : float
        The annual interest rate in percent (e.g., 5 for 5%).
    time : float
        The time period in years.

    Returns
    -------
    float
        The simple interest amount.
    """
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if rate < 0:
        raise ValueError("Rate cannot be negative.")
    if time < 0:
        raise ValueError("Time period cannot be negative.")

    return (principal * rate * time) / 100.0


if __name__ == "__main__":
    try:
        principal_input = float(input("Enter the principal amount: "))
        rate_input = float(input("Enter the annual interest rate (in %): "))
        time_input = float(input("Enter the time period in years: "))
        interest = calculate_simple_interest(principal_input, rate_input, time_input)
        print(f"Simple Interest: {interest:.2f}")
    except ValueError as e:
        print(f"Error: {e}")