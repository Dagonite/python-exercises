"""
Write a function that takes in a positive integer and returns its multiplicative
persistence, which is the number of times you must multiply the digits in the
integer until you reach a single digit.

For example, 39 should return 3:
3 * 9 = 27
2 * 7 = 14
1 * 4 = 4

999 should return 4:
9 * 9 * 9 = 729
7 * 2 * 9 = 126
1 * 2 * 6 = 12
1 * 2     = 2
"""

from functools import reduce
from operator import mul


def multiplicative_persistence(n):
    splits = 0
    while n >= 10:
        n = reduce(mul, [int(x) for x in str(n)], 1)
        splits += 1

    return splits


if __name__ == "__main__":
    test_cases = [
        55,
        22,
        8,
        999,
        1246,
        838324,
        6788,
    ]

    answers = [
        3,
        1,
        0,
        4,
        3,
        2,
        6,
    ]

    for i, test_case in enumerate(test_cases):
        res = multiplicative_persistence(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
