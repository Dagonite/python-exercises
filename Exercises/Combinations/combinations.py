# combinations.py
"""Create a function that takes a variable number of arguments, each argument representing the number of items in a 
group, and returns the number of permutations (combinations) of items that you could get by taking one item from each 
group. Input may include the number zero."""

from functools import reduce


def combinations(*items):
    return reduce(lambda x, y: (1 if not x else x) * (1 if not y else y), items)


print(combinations(2, 0, 6, 0, 5))
print(combinations(0, 2, 3, 4, 0, 5))
print(combinations(2, 3, 1, 0, 2, 5, 9, 0))
