def reverse_words(text):
    """Odwraca kolejność słów w podanym tekście."""
    return " ".join(text.split()[::-1])


def find_unique_words(text):
    """Zwraca zbiór unikalnych słów w tekście."""
    return set(text.lower().split())


from collections import Counter

def word_frequency(text):
    """Zwraca słownik częstotliwości występowania słów w tekście."""
    words = text.lower().split()
    return Counter(words)

def replace_vowels(text, char):
    """Zamienia samogłoski w tekście na podany znak."""
    vowels = "aeiouAEIOU"
    return ''.join([char if c in vowels else c for c in text])

def longest_word(text):
    """Znajduje najdłuższe słowo w podanym tekście."""
    words = text.split()
    return max(words, key=len) if words else ''

from my_awesome_lib.text_processing import replace_vowels
print(replace_vowels("Hello World", "*"))  # Output: "H*ll* W*rld"

