"""Given a list, nums, return the running sum of nums."""

# could also use accumulate() from itertools
def running_sum(nums):
    i = 1
    while i < len(nums):
        nums[i] += nums[i - 1]
        i += 1
    return nums


if __name__ == "__main__":
    test_cases = [[1, 2, 3, 4], [4, 5, 12, 11]]

    answers = [[1, 3, 6, 10], [4, 9, 21, 32]]

    for i, test_case in enumerate(test_cases):
        res = running_sum(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
