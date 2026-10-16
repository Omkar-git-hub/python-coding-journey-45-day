def count_vowels(s: str) -> int:
    """
    Count the number of vowels in the given string.

    Vowels considered are: a, e, i, o, u (both uppercase and lowercase).

    Parameters
    ----------
    s : str
        The input string to be evaluated.

    Returns
    -------
    int
        The total count of vowels in the string.
    """
    return sum(1 for char in s.lower() if char in "aeiou")


if __name__ == "__main__":
    # When executed directly, read a line from standard input and print the vowel count.
    input_string = input()
    print(count_vowels(input_string))