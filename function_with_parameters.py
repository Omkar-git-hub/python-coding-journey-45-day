def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob", "Hi"))