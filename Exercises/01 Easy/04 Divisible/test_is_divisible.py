# test_is_divisible.py
"""Unit testing for the is_divisible function."""

import unittest
from is_divisible import is_divisible


class TestDivisbleNumbers(unittest.TestCase):
    def test_is_divisible_true(self):
        self.assertTrue(is_divisible(5))
        self.assertTrue(is_divisible(14))
        self.assertTrue(is_divisible(86))
        self.assertTrue(is_divisible(194))
        self.assertTrue(is_divisible(293))

    def test_is_divisible_false(self):
        self.assertFalse(is_divisible(10))
        self.assertFalse(is_divisible(13))
        self.assertFalse(is_divisible(115))
        self.assertFalse(is_divisible(120))


if __name__ == "__main__":
    unittest.main()