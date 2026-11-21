def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."

def convert_to_integer(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Could not convert value to integer."
    except TypeError:
        return "Error: Invalid type for conversion."

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."
    except TypeError:
        return "Error: Invalid index type."

def main():
    # Test divide_numbers
    print(divide_numbers(10, 2))  # 5.0
    print(divide_numbers(10, 0))  # Error: Division by zero is not allowed.
    print(divide_numbers("10", 2))  # Error: Both arguments must be numbers.

    # Test convert_to_integer
    print(convert_to_integer("42"))  # 42
    print(convert_to_integer("hello"))  # Error: Could not convert value to integer.
    print(convert_to_integer(None))  # Error: Invalid type for conversion.

    # Test access_list_element
    my_list = [1, 2, 3, 4, 5]
    print(access_list_element(my_list, 2))  # 3
    print(access_list_element(my_list, 10))  # Error: Index out of range.
    print(access_list_element(my_list, "a"))  # Error: Invalid index type.

if __name__ == "__main__":
    main()