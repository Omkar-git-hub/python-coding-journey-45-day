def check_prime_number(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if check_prime_number(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")