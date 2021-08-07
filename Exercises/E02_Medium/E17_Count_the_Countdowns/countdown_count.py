"""
Create a function which takes an array, the length of the array, and a countdown 
start value, K. A contiguous subarray is an m-countdown if it is of length m and 
contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, 
[3, 2, 1] is a 3-countdown. This function should return a count of the number of 
K-countdowns in the array.
"""


def countdown_count(array, array_length, K):
    ans_counter = 0
    dec_counter = 0
    for i in range(1, array_length):
        if array[i] == array[i - 1] - 1:
            dec_counter += 1
        else:
            dec_counter = 0
        if array[i] == 1 and dec_counter >= K - 1:
            ans_counter += 1
    return ans_counter


if __name__ == "__main__":
    test_cases = [
        ([101, 100, 99, 98], 4, 2),
        ([1, 2, 3, 7, 9, 3, 2, 1, 8, 3, 2, 1], 12, 3),
        ([100, 7, 6, 5, 4, 3, 2, 1, 100], 9, 6),
    ]

    answers = [
        0,
        2,
        1,
    ]

    for i, (array, array_length, K) in enumerate(test_cases):
        res = countdown_count(array, array_length, K)
        print("[PASS]" if answers[i] == res else "[FAIL]", f"countdown_count({array}, {array_length}, {K}) = {res}")
