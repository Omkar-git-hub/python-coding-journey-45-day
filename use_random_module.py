import random

def generate_random_integer(min_val, max_val):
    return random.randint(min_val, max_val)

def generate_random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def generate_random_choice(options):
    return random.choice(options)

def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

def generate_random_sample(lst, k):
    return random.sample(lst, k)

def main():
    print("Random Module Examples")
    print("-" * 20)
    
    # Generate random integer
    rand_int = generate_random_integer(1, 100)
    print(f"Random integer between 1 and 100: {rand_int}")
    
    # Generate random float
    rand_float = generate_random_float(0.0, 1.0)
    print(f"Random float between 0.0 and 1.0: {rand_float:.4f}")
    
    # Generate random choice
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    random_fruit = generate_random_choice(fruits)
    print(f"Random fruit: {random_fruit}")
    
    # Shuffle a list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled_numbers = shuffle_list(numbers)
    print(f"Original list: {numbers}")
    print(f"Shuffled list: {shuffled_numbers}")
    
    # Generate random sample
    sample = generate_random_sample(numbers, 3)
    print(f"Random sample of 3 numbers: {sample}")
    
    # Generate random dice roll
    dice_roll = generate_random_integer(1, 6)
    print(f"Dice roll: {dice_roll}")
    
    # Generate random password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password_length = 12
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"Random password: {password}")

if __name__ == "__main__":
    main()