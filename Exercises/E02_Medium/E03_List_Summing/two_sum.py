"""
Write a program that finds the index of two numbers in a sorted array that sum
to a target. If no combination exists, return [-1, -1, -1].
"""


def two_sum(arr, target):
    """Solution that uses two pointers."""
    left = 0
    right = len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return [left, right]
    return [-1, -1, -1]


if __name__ == "__main__":
    test_cases = [
        ([-8, -2, 2, 4, 6], 4),
        ([-3, -1, 0, 1, 2, 5, 6], 7),
        ([-4, -1, 3, 4, 5, 5, 6], 10),
        ([-4, -1, 3, 4, 5], -5),
        ([-5, -3, 3, 5, 7], 6),
    ]

    answers = [
        [1, 4],
        [3, 6],
        [3, 6],
        [0, 1],
        [-1, -1, -1],
    ]

    for i, test_case in enumerate(test_cases):
        res = two_sum(test_case[0], test_case[1])
        print([answers[i] == res], res)
