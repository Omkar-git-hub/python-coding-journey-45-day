def count_word_frequency(text):
    """
    Count the frequency of each word in the given text.
    
    Args:
        text (str): The input text to analyze.
        
    Returns:
        dict: A dictionary where keys are words (lowercase) and values are their frequencies.
    """
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Count frequency of each word
    frequency = {}
    for word in words:
        # Remove punctuation from the word
        cleaned_word = word.strip(".,!?;:'\"()[]{}")
        if cleaned_word:  # Only count non-empty words
            frequency[cleaned_word] = frequency.get(cleaned_word, 0) + 1
    
    return frequency


if __name__ == "__main__":
    # Example usage
    sample_text = "Hello world, hello Python. Python is great, and hello world is awesome."
    print("Text:", sample_text)
    print("\nWord Frequencies:")
    freq = count_word_frequency(sample_text)
    for word, count in sorted(freq.items()):
        print(f"  {word}: {count}")