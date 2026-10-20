def create_list(n):
    """
    Create and return a list of integers from 1 to n (inclusive).

    Parameters:
        n (int): The upper bound of the list. Must be a positive integer.

    Returns:
        list[int]: List containing numbers from 1 to n.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    return list(range(1, n + 1))


if __name__ == "__main__":
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)
        result = create_list(number)
        print(result)
    except ValueError:
        print("Invalid input: please enter a valid positive integer")
    except TypeError as e:
        print(f"Error: {e}")