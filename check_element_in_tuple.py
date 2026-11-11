def check_element_in_tuple(element, my_tuple):
    if element in my_tuple:
        return True
    return False

if __name__ == "__main__":
    sample_tuple = (10, 20, 30, 40, 50)
    element_to_check = 30
    
    if check_element_in_tuple(element_to_check, sample_tuple):
        print(f"{element_to_check} is present in the tuple.")
    else:
        print(f"{element_to_check} is not present in the tuple.")