original_dict = {"name": "Alice", "age": 30, "city": "New York"}
copied_dict = original_dict.copy()

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

original_dict["age"] = 31
print("\nAfter modifying original dictionary:")
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)