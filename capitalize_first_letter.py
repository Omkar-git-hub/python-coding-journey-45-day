def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == "__main__":
    sample = "hello world"
    print(capitalize_first_letter(sample))