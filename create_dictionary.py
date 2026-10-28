def create_dictionary():
    """
    Create and return a dictionary with sample key-value pairs.

    Returns:
        dict: A dictionary containing example data.
    """
    return {
        "name": "Alice",
        "age": 28,
        "city": "Wonderland",
        "is_student": False,
        "scores": [85, 92, 78]
    }

if __name__ == "__main__":
    print(create_dictionary())