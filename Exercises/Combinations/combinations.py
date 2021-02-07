# combinations.py
"""Create a function that takes a variable number of arguments, each argument representing the number of items in a 
group, and returns the number of permutations (combinations) of items that you could get by taking one item from each 
group. Input may include the number zero."""

from functools import reduce


def combinations(*items):
    return reduce(lambda x, y: (1 if not x else x) * (1 if not y else y), items)


if __name__ == "__main__":
    test_cases = [
        (2, 0, 6, 0, 5),
        (0, 2, 3, 4, 0, 5),
        (2, 3, 1, 0, 2, 5, 9, 0),
        (2, 3, 6, 5, 3, 4, 1, 1, 2),
    ]

    answers = [
        60,
        120,
        540,
        4320,
    ]

    for i, test_case in enumerate(test_cases):
        res = combinations(*test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)