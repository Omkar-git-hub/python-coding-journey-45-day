def find_last_character(text):
    if not text:
        return ""
    return text[-1]

if __name__ == "__main__":
    sample = "Hello, World!"
    print(f"Last character of '{sample}': {find_last_character(sample)}")