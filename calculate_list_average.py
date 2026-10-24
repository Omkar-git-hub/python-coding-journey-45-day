def calculate_list_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_list_average(sample_list)
    print(f"List: {sample_list}")
    print(f"Average: {average}")