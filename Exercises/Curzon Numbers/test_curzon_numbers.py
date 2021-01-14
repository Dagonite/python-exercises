# test_curzon_numbers.py
"""Unit testing for Curzon numbers."""

import unittest
import curzon_numbers


class TestCurzonNumbers(unittest.TestCase):
    def test_is_curzon_true(self):
        self.assertTrue(curzon_numbers.is_curzon(5))
        self.assertTrue(curzon_numbers.is_curzon(14))
        self.assertTrue(curzon_numbers.is_curzon(86))
        self.assertTrue(curzon_numbers.is_curzon(194))
        self.assertTrue(curzon_numbers.is_curzon(293))

    def test_is_curzon_false(self):
        self.assertFalse(curzon_numbers.is_curzon(10))
        self.assertFalse(curzon_numbers.is_curzon(13))
        self.assertFalse(curzon_numbers.is_curzon(115))
        self.assertFalse(curzon_numbers.is_curzon(120))


if __name__ == "__main__":
    unittest.main()