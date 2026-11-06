def check_number_less_than_100(number):
    if number < 100:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if check_number_less_than_100(num):
        print(f"{num} is less than 100")
    else:
        print(f"{num} is not less than 100")