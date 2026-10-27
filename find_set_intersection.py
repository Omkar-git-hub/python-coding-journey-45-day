def find_set_intersection(set1, set2):
    """
    Find the intersection of two sets.
    
    Args:
        set1: First set
        set2: Second set
        
    Returns:
        A set containing elements common to both sets
    """
    return set1.intersection(set2)

if __name__ == "__main__":
    # Example usage
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    intersection = find_set_intersection(set1, set2)
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Intersection: {intersection}")