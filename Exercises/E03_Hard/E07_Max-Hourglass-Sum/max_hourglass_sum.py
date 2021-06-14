# max_hourglass_sum.py
"""Given a 6x6 2d array, an hourglass is a subset of values with indices falling in this pattern within the array:

a b c
  d  
e f g

There are 16 hourglasses in the array. An hourglass sum is the sum of an hourglass's values. Write a function to
calculate the hourglass sum for every hourglass in the array, then return the maximum hourglass sum."""


def max_hourglass_sum(arr):
    hourglasses = (hourglass(arr, i, j) for i in range(len(arr[0]) - 2) for j in range(len(arr) - 2))
    return max(sum(glass) for glass in hourglasses)


def hourglass(arr, x, y):
    yield from arr[x][y : y + 3]
    yield arr[x + 1][y + 1]
    yield from arr[x + 2][y : y + 3]


if __name__ == "__main__":
    test_cases = [
        [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ],
        [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 9, 2, -4, -4, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0],
        ],
        [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ],
    ]

    answers = [
        19,  # 2 4 4 2 1 2 4
        13,  # 0 1 0 1 0 9 2
        28,  # 0 4 3 1 8 6 6
    ]

    for i, test_case in enumerate(test_cases):
        res = max_hourglass_sum(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
