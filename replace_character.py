def replace_character(text, old_char, new_char):
    """
    Replaces all occurrences of a character in a string with another character.

    Args:
        text (str): The original string.
        old_char (str): The character to be replaced.
        new_char (str): The character to replace with.

    Returns:
        str: The modified string.
    """
    return text.replace(old_char, new_char)

if __name__ == "__main__":
    sample_text = "Hello World"
    old_char = "o"
    new_char = "0"
    result = replace_character(sample_text, old_char, new_char)
    print(f"Original: {sample_text}")
    print(f"Replaced '{old_char}' with '{new_char}': {result}")