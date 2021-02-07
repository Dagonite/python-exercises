# is_sastry.py
"""Establish if a given integer, n, is a Sastry number. If the number resulting from the concatenation of an integer n 
with its successor is a perfect square, then n is a Sastry Number. Given a positive integer n, implement a function that 
returns True if n is a Sastry number, or False if it's not.

You can expect only valid positive integers greater than 0 as input, without exceptions to handle."""


def is_sastry(n):
    """Return true if n concatenated with n + 1 is a perfect square."""
    square_root = int(str(n) + str(n + 1)) ** 0.5
    return square_root == int(square_root)


def is_sastry_mod(n):
    """Modulus version of above function."""
    return int(str(n) + str(n + 1)) ** 0.5 % 1 == 0


print(is_sastry_mod(183))
print(is_sastry_mod(11))
print(is_sastry_mod(32))
print(is_sastry_mod(0))
