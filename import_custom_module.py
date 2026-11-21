from my_module import add

def add_numbers(a, b):
    """
    Add two numbers using the custom module `my_module`.

    Parameters:
    a (int or float): First number.
    b (int or float): Second number.

    Returns:
    int or float: The sum of a and b obtained from `my_module.add`.
    """
    return add(a, b)

if __name__ == "__main__":
    # Example usage
    result = add_numbers(3, 5)
    print(f"The sum of 3 and 5 is {result}")