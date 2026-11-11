def unpack_tuple_elements():
    """
    Demonstrates unpacking tuple elements into variables.
    """
    # Create a tuple
    sample_tuple = (10, 20, 30)
    
    # Unpack the tuple into individual variables
    a, b, c = sample_tuple
    
    # Print the unpacked values
    print(f"First element: {a}")
    print(f"Second element: {b}")
    print(f"Third element: {c}")
    
    # Demonstrate unpacking with a different tuple
    name, age, city = ("Alice", 30, "New York")
    print(f"\nName: {name}, Age: {age}, City: {city}")
    
    # Demonstrate unpacking with a list (works similarly)
    x, y, z = [100, 200, 300]
    print(f"\nList unpacking - x: {x}, y: {y}, z: {z}")
    
    # Demonstrate unpacking with a string
    first, second, third = "Hello"
    print(f"\nString unpacking - {first}, {second}, {third}")


if __name__ == "__main__":
    unpack_tuple_elements()