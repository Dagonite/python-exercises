"""
Create a function that takes a number and returns its length without using the
len() function.
"""


def number_length(num):
    return sum(1 for _ in str(num))


if __name__ == "__main__":
    test_cases = [
        5,
        12,
        402,
        1230,
        63464,
        123532,
    ]

    answers = [
        1,
        2,
        3,
        4,
        5,
        6,
    ]

    for i, test_case in enumerate(test_cases):
        res = number_length(test_case)
        print([answers[i] == res], res)
