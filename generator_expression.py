def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create a generator expression that squares each number
    squares_gen = (x ** 2 for x in numbers)
    
    print("Generator Expression for Squares:")
    print("Generator object:", squares_gen)
    
    # Consume the generator
    print("Squares:", list(squares_gen))
    
    # Create another generator expression for even numbers
    even_gen = (x for x in numbers if x % 2 == 0)
    
    print("\nGenerator Expression for Even Numbers:")
    print("Generator object:", even_gen)
    
    # Consume the generator
    print("Even numbers:", list(even_gen))
    
    # Demonstrate lazy evaluation
    print("\nDemonstrating Lazy Evaluation:")
    lazy_gen = (x ** 2 for x in range(1, 6))
    print("Generator created:", lazy_gen)
    print("First value:", next(lazy_gen))
    print("Second value:", next(lazy_gen))
    print("Remaining values:", list(lazy_gen))

if __name__ == "__main__":
    main()