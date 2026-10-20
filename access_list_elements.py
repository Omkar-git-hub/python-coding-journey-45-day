def main():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("List of fruits:", fruits)
    print("First element:", fruits[0])
    print("Second element:", fruits[1])
    print("Last element:", fruits[-1])
    print("Second to last element:", fruits[-2])
    print("Slice (first three):", fruits[:3])
    print("Slice (last two):", fruits[-2:])
    print("Slice (middle):", fruits[1:4])

if __name__ == "__main__":
    main()