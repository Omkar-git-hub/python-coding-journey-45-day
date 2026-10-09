def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    -------
    float
        The area of the rectangle (length * width).

    Examples
    --------
    >>> calculate_rectangle_area(5, 3)
    15
    >>> calculate_rectangle_area(2.5, 4)
    10.0
    """
    return length * width


if __name__ == "__main__":
    # Simple interactive usage
    try:
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(l, w)
        print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")