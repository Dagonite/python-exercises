# closest_to_zero.py
"""Implement a function which takes a list of temperatures ts and returns the temperature closest to 0. If the list is 
empty, the function should return 0. If two temperatures are equally close to zero, the positive temperature must be 
returned. For example, if the input is -5 and 5, then 5 must be returned."""


def compute_closest_to_zero(ts):
    try:
        ts.sort(reverse=True)  # sort the list in descending order
        absolute_ts = [abs(t) for t in ts]  # create a list of absolute ts values
        min_t = min(absolute_ts)  # find the min t in ts
        min_t_index = absolute_ts.index(min_t)  # find the first index of min t
        return ts[min_t_index]
    except:
        return 0


if __name__ == "__main__":
    test_cases = [
        [7, 5, 9, 1, 4],
        [-273],
        [5526],
        [-15, -7, -9, -14, -12],
        [-10, -10],
        [],
        [15, -7, 9, 14, 7, 12],
    ]

    answers = [
        1,
        -273,
        5526,
        -7,
        -10,
        0,
        7,
    ]

    for i, test_case in enumerate(test_cases):
        res = compute_closest_to_zero(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)