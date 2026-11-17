def square_number(n):
    return n * n

def main():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square_number, numbers))
    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)

if __name__ == "__main__":
    main()