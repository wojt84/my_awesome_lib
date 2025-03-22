import unittest
from my_awesome_lib.text_processing import reverse_words, find_unique_words, word_frequency

class TestTextProcessing(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("Hello world"), "world Hello")
        self.assertEqual(reverse_words("Python is fun"), "fun is Python")

    def test_find_unique_words(self):
        self.assertEqual(find_unique_words("Python Python fun fun"), {"python", "fun"})
        self.assertEqual(find_unique_words(""), set())

    def test_word_frequency(self):
        self.assertEqual(word_frequency("Python is fun Python"), {"python": 2, "is": 1, "fun": 1})

if __name__ == "__main__":
    unittest.main()

    import unittest
from my_awesome_lib.text_processing import replace_vowels, longest_word

class TestTextProcessing(unittest.TestCase):
    def test_replace_vowels(self):
        self.assertEqual(replace_vowels("Hello World", "*"), "H*ll* W*rld")
        self.assertEqual(replace_vowels("Python", "#"), "Pyth#n")

    def test_longest_word(self):
        self.assertEqual(longest_word("The quick brown fox"), "quick")
        self.assertEqual(longest_word(""), '')

if __name__ == "__main__":
    unittest.main()

