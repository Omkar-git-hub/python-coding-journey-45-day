def count_words(text):
    if not text:
        return 0
    return len(text.split())

if __name__ == "__main__":
    sample_text = "Hello world, this is a test."
    word_count = count_words(sample_text)
    print(f"Number of words: {word_count}")