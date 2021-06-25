"""Assuming you have two integers, x and y, with y bigger than x. Sum all the numbers from x to y inclusively. Example: 
if x is 1 and y is 5, then sum 1+2+3+4+5."""


def sbr_imp(x, y):
    """Sum between range imperatively."""
    total = 0
    for n in range(x, y + 1):
        total += n
    return total


def sbr_reduce(x, y):
    """Sum between range using reduce() and lambda."""
    from functools import reduce

    return reduce(lambda n, m: n + m, range(x, y + 1))


def sbr_sum(x, y):
    "Sum between range using sum()."
    return sum([n for n in range(x, y + 1)])


if __name__ == "__main__":
    sbr_funcs = [
        sbr_imp,
        sbr_reduce,
        sbr_sum,
    ]

    test_cases = [
        (5, 10),
        (8, 11),
        (1, 4),
    ]

    answers = [
        45,
        38,
        10,
    ]

    def call_func(func):
        for i, test_case in enumerate(test_cases):
            res = func(test_case[0], test_case[1])
            print([answers[i] == res], res)

    for sbr_func in sbr_funcs:
        print(sbr_func.__doc__)
        call_func(sbr_func)
        print()