def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == "__main__":
    area = calculate_area(width=5, length=10)
    perimeter = calculate_perimeter(width=5, length=10)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")