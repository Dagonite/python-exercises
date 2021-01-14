# two_sum.py
"""Write a program that finds two numbers in a sorted array that sums to a target. If no combination exists, return 
None."""


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
            return [left, right], arr[left], arr[right]
    return None


print(two_sum([-8, -2, 2, 4, 6], 4))
print(two_sum([-3, -1, 0, 1, 2, 5, 6], 7))
print(two_sum([-4, -1, 3, 4, 5, 5, 6], 10))
print(two_sum([-4, -1, 3, 4, 5], -5))
print(two_sum([-5, -3, 3, 5, 7], 6))