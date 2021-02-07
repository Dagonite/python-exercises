# is_perfect_square.py
"""Create a function to establish if a given integer, n, concatenated with its successor is a perfect square. The 
function should return True or False."""


def is_perfect_square(n):
    """Return True if n concatenated with n + 1 is a perfect square."""
    return int(str(n) + str(n + 1)) ** 0.5 % 1 == 0


if __name__ == "__main__":
    test_cases = [
        183,
        11,
        32,
        106755,
    ]

    answers = [
        True,
        False,
        False,
        True,
    ]

    for i, test_case in enumerate(test_cases):
        res = is_perfect_square(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)