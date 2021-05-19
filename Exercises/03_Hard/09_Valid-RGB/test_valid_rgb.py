# test_valid_rgb.py

import valid_rgb
import unittest
from random import randrange, uniform


class TestValidColor(unittest.TestCase):
    def test_valid_rgb(self):
        for _ in range(50):
            r, g, b = [randrange(0, 256) for _ in range(3)]
            self.assertTrue(func(f"rgb({r},{g},{b})"))

    def test_valid_spaced_rgb(self):
        for _ in range(50):
            r, g, b = [randrange(0, 256) for _ in range(3)]
            self.assertTrue(func(f"rgb({r}, {g}, {b})"))

    def test_valid_rgb_percents(self):
        for _ in range(50):
            r, g, b = [randrange(0, 101) for _ in range(3)]
            self.assertTrue(func(f"rgb({r}%,{g}%,{b}%)"))

    def test_valid_spaced_rgb_percents(self):
        for _ in range(50):
            r, g, b = [randrange(0, 101) for _ in range(3)]
            self.assertTrue(func(f"rgb({r}%, {g}%, {b}%)"))

    def test_valid_mixed_rgb_values(self):
        for _ in range(10):
            r, g, b = randrange(0, 101), randrange(0, 101), randrange(0, 256)
            self.assertTrue(func(f"rgb({r}%,{g}%,{b})"))

        for _ in range(10):
            r, g, b = randrange(0, 256), randrange(0, 101), randrange(0, 256)
            self.assertTrue(func(f"rgb({r},{g}%,{b})"))

        for _ in range(10):
            r, g, b = randrange(0, 101), randrange(0, 256), randrange(0, 256)
            self.assertTrue(func(f"rgb({r}%,{g},{b})"))

        for _ in range(10):
            r, g, b = randrange(0, 101), randrange(0, 256), randrange(0, 101)
            self.assertTrue(func(f"rgb({r}%,{g},{b}%)"))

        for _ in range(10):
            r, g, b = randrange(0, 256), randrange(0, 101), randrange(0, 101)
            self.assertTrue(func(f"rgb({r},{g}%,{b}%)"))

    def test_invalid_rgb(self):
        for _ in range(25):
            r, g, b = [randrange(-(10 ** 8), 0) for _ in range(3)]
            self.assertFalse(func(f"rgb({r},{g},{b})"))

        for _ in range(25):
            r, g, b = [randrange(255, 10 ** 8) for _ in range(3)]
            self.assertFalse(func(f"rgb({r},{g},{b})"))

    def test_invalid_rgb_percents(self):
        for _ in range(25):
            r, g, b = [randrange(-(10 ** 8), 0) for _ in range(3)]
            self.assertFalse(func(f"rgb({r}%,{g}%,{b}%)"))

        for _ in range(25):
            r, g, b = [randrange(101, 10 ** 8) for _ in range(3)]
            self.assertFalse(func(f"rgb({r}%,{g}%,{b}%)"))

    def test_valid_rgba(self):
        for _ in range(50):
            (r, g, b), a = [randrange(0, 256) for _ in range(3)], uniform(0, 1)
            self.assertTrue(func(f"rgba({r},{g},{b},{a})"))

    def test_valid_rgba_percents(self):
        for _ in range(50):
            (r, g, b), a = [randrange(0, 101) for _ in range(3)], uniform(0, 1)
            self.assertTrue(func(f"rgba({r}%,{g}%,{b}%,{a})"))

    def test_valid_mixed_rgba_values(self):
        for _ in range(10):
            r, g, b, a = randrange(0, 101), randrange(0, 101), randrange(0, 256), uniform(0, 1)
            self.assertTrue(func(f"rgba({r}%,{g}%,{b},{a})"))

        for _ in range(10):
            r, g, b, a = randrange(0, 101), randrange(0, 101), randrange(0, 256), uniform(0, 1)
            self.assertTrue(func(f"rgba({r}%,{g}%,{b},{a})"))

        for _ in range(10):
            r, g, b, a = randrange(0, 256), randrange(0, 256), randrange(0, 256), uniform(0, 1)
            self.assertTrue(func(f"rgba({r},{g},{b},{a})"))

    def test_invalid_rgba(self):
        for _ in range(25):
            (r, g, b), a = [randrange(-(10 ** 8), 0) for _ in range(3)], uniform(-1, 2)
            self.assertFalse(func(f"rgba({r},{g},{b},{a})"))

        for _ in range(25):
            (r, g, b), a = [randrange(255, 10 ** 8) for _ in range(3)], uniform(-1, 2)
            self.assertFalse(func(f"rgba({r},{g},{b},{a})"))

    def test_invalid_rgba_percents(self):
        for _ in range(25):
            (r, g, b), a = [randrange(-(10 ** 8), 0) for _ in range(3)], uniform(0, 1)
            self.assertFalse(func(f"rgba({r}%,{g}%,{b}%,{a})"))

        for _ in range(25):
            (r, g, b), a = [randrange(101, 10 ** 8) for _ in range(3)], uniform(0, 1)
            self.assertFalse(func(f"rgba({r}%,{g}%,{b}%,{a})"))


if __name__ == "__main__":
    func = valid_rgb.valid_color
    unittest.main()
