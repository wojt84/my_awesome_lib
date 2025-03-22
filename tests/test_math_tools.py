import unittest
from my_awesome_lib.math_tools import is_prime, gcd, calculate_mean

class TestMathTools(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    def test_gcd(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(7, 3), 1)

    def test_calculate_mean(self):
        self.assertEqual(calculate_mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(calculate_mean([]), 0)

if __name__ == "__main__":
    unittest.main()

import unittest
from my_awesome_lib.math_tools import lcm, generate_fibonacci

class TestMathTools(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(6, 8), 24)
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(7, 3), 21)

    def test_generate_fibonacci(self):
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci(0), [])
        self.assertEqual(generate_fibonacci(1), [0])

if __name__ == "__main__":
    unittest.main()

