# parity_outlier.py
"""Write a function that takes a list of at least 3 numbers. The function must return the single odd or even number in 
the list."""


def parity_outlier(numbers):
    odds = [x for x in numbers if x % 2]
    evens = [x for x in numbers if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


if __name__ == "__main__":
    test_cases = [
        [2, 6, 8, 10, 3],  # odd at the back
        [2, 6, 8, 200, 700, 1, 84, 10, 4],  # odd in the middle
        [17, 6, 8, 10, 6, 12, 24, 36],  # odd in the front
        [2, 1, 7, 17, 19, 211, 7],  # even in the front
        [1, 1, 1, 1, 1, 44, 7, 7, 7, 7, 7, 7, 7, 7],  # even in the middle
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 1000],  # even at the end
        [2, -6, 8, -10, -3],  # odd at the back, negative
        [2, 6, 8, 2, -66, 34, -35, 66, 700, 1002, -84, 10, 4],  # odd in the middle, negative
        [-123456789, -18, 6, -8, -10, 6, 12, -24, 36],  # odd in the front, negative
        [-20, 1, 7, 17, 19, 211, 7],  # even in the front, negative
        [1, 1, -1, 1, 1, -44, 7, 7, 7, 7, 7, 7, 7, 7],  # even in the middle, negative
        [1, 0, 0],  # odd answer, zeroes
        [3, 7, -99, 81, 90211, 0, 7],  # even in the middle, zero
    ]

    answers = [
        3,
        1,
        17,
        2,
        44,
        1000,
        -3,
        -35,
        -123456789,
        -20,
        -44,
        1,
        0,
    ]

    for i, test_case in enumerate(test_cases):
        res = parity_outlier(test_case)
        print([answers[i] == res], res)
