def loop_through_dictionary():
    """
    Demonstrates how to loop through a dictionary in Python.
    """
    # Create a sample dictionary
    student_info = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8
    }
    
    print("Looping through dictionary keys:")
    for key in student_info:
        print(f"Key: {key}")
    
    print("\nLooping through dictionary values:")
    for value in student_info.values():
        print(f"Value: {value}")
    
    print("\nLooping through dictionary items:")
    for key, value in student_info.items():
        print(f"{key}: {value}")
    
    return student_info

if __name__ == "__main__":
    loop_through_dictionary()