import unittest
from my_awesome_lib.data_utils import filter_by_type, normalize_numbers

class TestDataUtils(unittest.TestCase):
    def test_filter_by_type(self):
        self.assertEqual(filter_by_type([1, "abc", 2.5, True], int), [1])
        self.assertEqual(filter_by_type([1, "abc", 2.5, True], str), ["abc"])

    def test_normalize_numbers(self):
        self.assertEqual(normalize_numbers([1, 2, 3]), [0.3333333333333333, 0.6666666666666666, 1.0])
        self.assertEqual(normalize_numbers([]), [])

if __name__ == "__main__":
    unittest.main()

import unittest
from my_awesome_lib.data_utils import remove_duplicates, split_list

class TestDataUtils(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])
        self.assertEqual(remove_duplicates(["a", "b", "a", "c"]), ["a", "b", "c"])

    def test_split_list(self):
        self.assertEqual(split_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(split_list([], 3), [])

if __name__ == "__main__":
    unittest.main()
