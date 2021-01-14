# curzon_numbers.py
"""Write a program to establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly 
divisible by 1 plus 2 multiplied by num, then num is a Curzon number. Given a non-negative integer num, implement a 
function that returns True if num is a Curzon number, or False otherwise."""


def is_curzon(num):
    return not (2 ** num + 1) % (2 * num + 1)