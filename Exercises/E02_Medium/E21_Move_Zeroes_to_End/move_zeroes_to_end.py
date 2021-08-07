"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
"""


def move_zeroes(arr):
    new_arr = [i for i in arr if i is False or i != 0]
    zero_arr = [0] * (len(arr) - len(new_arr))
    return new_arr + zero_arr


if __name__ == "__main__":
    test_cases = [
        [0, 1],
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 1, 7, 8, 0, 5],
        ["0", 0, "1"],
        [1, False, True, 0, 2, 30, 4, "house", 5, 0, 0.0, "car", 5, 0],
    ]

    answers = [
        [1, 0],
        [1, 1, 0],
        [0, 0, 0],
        [1, 7, 8, 5, 0, 0, 0],
        ["0", "1", 0],
        [1, False, True, 2, 30, 4, "house", 5, "car", 5, 0, 0, 0, 0],
    ]

    for i, test_case in enumerate(test_cases):
        res = move_zeroes(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
