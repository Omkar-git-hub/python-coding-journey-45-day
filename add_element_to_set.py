def add_element_to_set(sample_set, element):
    sample_set.add(element)
    return sample_set

if __name__ == "__main__":
    my_set = {1, 2, 3}
    new_element = 4
    updated_set = add_element_to_set(my_set, new_element)
    print(f"Original set: {my_set}")
    print(f"Element to add: {new_element}")
    print(f"Updated set: {updated_set}")