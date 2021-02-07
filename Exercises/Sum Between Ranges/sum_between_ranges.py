# sum_between_ranges.py
"""Assuming you have two integers, x and y, with y bigger than x. Sum all the numbers from x to y inclusively. Example: 
if x is 1 and y is 5, then sum 1+2+3+4+5."""

from functools import reduce

x = 5
y = 10

# basic way
def sum_between_two_ints(x, y):
    total = 0
    for n in range(x, y + 1):
        total += n
    return total


print(sum_between_two_ints(x, y))


# using reduce and lambda
print(reduce(lambda n, m: n + m, range(x, y + 1)))