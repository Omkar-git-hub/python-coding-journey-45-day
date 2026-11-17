numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squares using list comprehension
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Create a list of even numbers using list comprehension
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# Create a list of odd numbers using list comprehension
odds = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odds)

# Create a list of numbers greater than 5
greater_than_5 = [n for n in numbers if n > 5]
print("Numbers greater than 5:", greater_than_5)

# Create a list of numbers less than 5
less_than_5 = [n for n in numbers if n < 5]
print("Numbers less than 5:", less_than_5)

# Create a list of numbers divisible by 3
divisible_by_3 = [n for n in numbers if n % 3 == 0]
print("Numbers divisible by 3:", divisible_by_3)

# Create a list of numbers divisible by 4
divisible_by_4 = [n for n in numbers if n % 4 == 0]
print("Numbers divisible by 4:", divisible_by_4)

# Create a list of numbers between 3 and 7 (exclusive)
between_3_and_7 = [n for n in numbers if 3 < n < 7]
print("Numbers between 3 and 7:", between_3_and_7)

# Create a list of numbers that are perfect squares
perfect_squares = [n for n in numbers if n ** 0.5 == int(n ** 0.5)]
print("Perfect squares:", perfect_squares)

# Create a list of numbers that are not perfect squares
not_perfect_squares = [n for n in numbers if n ** 0.5 != int(n ** 0.5)]
print("Not perfect squares:", not_perfect_squares)