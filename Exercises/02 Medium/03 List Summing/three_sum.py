# three_sum.py
"""Write a program that finds three numbers in a sorted array that sums to a target. If no combination exists, return 
None."""


def three_sum(arr, target):
    for i, n in enumerate(arr):
        left = i + 1
        adjusted_target = target - n
        right = len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total < adjusted_target:
                left += 1
            elif total > adjusted_target:
                right -= 1
            else:
                return [i, left, right], (n, arr[left], arr[right])
    return None


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 4], 5),
        ([1, 4, 5, 5, 6, 11], 18),
        ([2, 4, 5, 6, 6, 6, 7, 17], 30),
        ([1, 2, 4, 5, 12, 17, 18, 20], 34),
        ([1, 8, 9, 11, 12, 17, 18, 20, 21], 57),
    ]

    answers = [
        ([0, 1, 2], (1, 2, 2)),
        ([0, 4, 5], (1, 6, 11)),
        ([3, 6, 7], (6, 7, 17)),
        ([1, 4, 7], (2, 12, 20)),
        None,
    ]

    for i, test_case in enumerate(test_cases):
        res = three_sum(test_case[0], test_case[1])
        print([answers[i] == res], res)