"""
This module demonstrates importing a built-in Python module.
It imports the `math` module and provides a simple function
to calculate the area of a circle given its radius.
"""

import math


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle using the math module.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2


if __name__ == "__main__":
    # Example usage
    try:
        r = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(r)
        print(f"The area of the circle with radius {r} is {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")