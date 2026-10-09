import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Parameters
    ----------
    radius : float
        The radius of the circle. Must be a non-negative number.

    Returns
    -------
    float
        The area of the circle.

    Raises
    ------
    ValueError
        If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius * radius

__all__ = ["calculate_circle_area"]