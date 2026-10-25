def access_tuple_elements():
    """
    Creates a tuple and accesses its elements by index.
    """
    sample_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    
    print("Original Tuple:", sample_tuple)
    print("First element:", sample_tuple[0])
    print("Second element:", sample_tuple[1])
    print("Last element:", sample_tuple[-1])
    print("Elements from index 1 to 3:", sample_tuple[1:4])
    
    return sample_tuple

if __name__ == "__main__":
    access_tuple_elements()