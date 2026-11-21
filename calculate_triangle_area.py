def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    base (float): The length of the base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

# Alias for compatibility with potential alternative naming
calculate_area_of_triangle = calculate_triangle_area