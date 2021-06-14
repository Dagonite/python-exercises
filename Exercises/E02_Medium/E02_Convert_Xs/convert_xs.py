# convert_xs.py
"""Write a function that takes a string of at least 3 characters comprising of "X"s and "."s. The function should return 
the smallest number of changes that would be needed to make every character a dot. Up to three connected "X"s can be
converted at once."""

from math import ceil


def convert_xs(string):
    groups = string.split(".")

    return sum(ceil(len(group) / 3) for group in groups)


if __name__ == "__main__":
    test_cases = [
        "XXX",
        "...",
        "X.X",
        ".X.",
        "XX.XX",
        "X.X.X.X.X",
        "XXXX.X",
    ]

    answers = [
        1,
        0,
        2,
        1,
        2,
        5,
        3,
    ]

    for i, test_case in enumerate(test_cases):
        res = convert_xs(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)