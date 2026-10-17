def count_consonants(s: str) -> int:
    """
    Count the number of consonant letters in the given string.

    Consonants are defined as alphabetic characters that are not vowels
    (a, e, i, o, u) regardless of case. Non‑alphabetic characters are ignored.

    Args:
        s: Input string.

    Returns:
        The count of consonant characters in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch.isalpha() and ch not in vowels)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(count_consonants(user_input))