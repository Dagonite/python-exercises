"""
Write a program that will calculate the number of trailing zeros in a factorial
of a given number.
"""


def zeroes(n):
    x = n // 5
    return x + zeroes(x) if x else 0


if __name__ == "__main__":
    test_cases = [
        0,  # 0! = 1
        1,  # 1! = 1
        2,  # 2! = 2
        6,  # 6! = 720
        12,  # 12! = 479_001_600
        29,  # 29! = 8_841_761_993_739_701_954_543_616_000_000
        31,  # 31! = 8_222_838_654_177_922_817_725_562_880_000_000
    ]

    answers = [
        0,
        0,
        0,
        1,
        2,
        6,
        7,
    ]

    for i, test_case in enumerate(test_cases):
        res = zeroes(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
