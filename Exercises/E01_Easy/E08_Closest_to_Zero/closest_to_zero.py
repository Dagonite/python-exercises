"""Implement a function which takes a list of temperatures ts and returns the temperature closest to 0. If the list is 
empty, the function should return 0. If two temperatures are equally close to zero, the positive temperature must be 
returned. For example, if the input is -5 and 5, then 5 must be returned."""


def compute_closest_to_zero(ts):
    try:
        closest = ts[0]  # set closest to first value in ts
        for t in ts:  # iterate over values in ts
            abs_closest = abs(closest)
            abs_t = abs(t)
            if abs_t < abs_closest:
                closest = t  # if t is closer to 0 than closest, set closest as t
            elif abs_t == abs_closest and t != closest:
                closest = abs_t  # if t and closest have same abs but are different, set closest to abs_t
        return closest
    except:
        return 0  # return 0 if ts empty


if __name__ == "__main__":
    test_cases = [
        [7, 5, 9, 1, 4],
        [-273],
        [5526],
        [-15, -7, -9, -14, -12],
        [-10, -10],
        [],
        [15, -7, 9, 14, 7, 12],
        [11, -11, 13, 13, 12, 11, -5, 5, 5, 21, 32, 30, -9, 20, -8, 11, 15, 11, -8, 3, 4, -5, -6, 7],
        [18, -1, -15, 11, 18, 2, 1, -8, 5, 5, 35, 32, -5, -9, 18],
    ]

    answers = [
        1,
        -273,
        5526,
        -7,
        -10,
        0,
        7,
        3,
        1,
    ]

    for i, test_case in enumerate(test_cases):
        res = compute_closest_to_zero(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)