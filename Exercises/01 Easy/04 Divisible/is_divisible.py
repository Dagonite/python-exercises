# is_divisible.py
"""Create a function to establish if 1 + 2 elevated to a given integer, n, is exactly divisible by 1 + 2 multiplied by 
n."""


def is_divisible(num):
    return not (2 ** num + 1) % (2 * num + 1)