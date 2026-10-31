import re
from collections import Counter
from typing import Dict, Tuple


def _clean_text(text: str) -> list:
    """
    Helper to split the input text into words.
    Words are defined as sequences of alphanumeric characters.
    The function lower‑cases the words to make the count case‑insensitive.
    """
    # Use regex to find words (alphanumeric + underscore)
    words = re.findall(r"\b\w+\b", text.lower())
    return words


def find_most_frequent_word(text: str) -> str:
    """
    Return the most frequent word in the given text.

    The function is case‑insensitive and ignores punctuation.
    If multiple words share the highest frequency, the word that appears
    first in the original text (ignoring case) is returned.
    An empty string is returned for empty input.

    Parameters
    ----------
    text: str
        The input string to analyse.

    Returns
    -------
    str
        The most frequent word, or an empty string if ``text`` is empty.
    """
    if not text:
        return ""

    # Preserve original order of appearance (case‑insensitive)
    original_words = _clean_text(text)

    if not original_words:
        return ""

    frequency: Dict[str, int] = Counter(original_words)

    # Determine the highest frequency
    max_freq = max(frequency.values())

    # Find the first word in the original order that has the max frequency
    for word in original_words:
        if frequency[word] == max_freq:
            return word

    # Fallback (should never be reached)
    return ""