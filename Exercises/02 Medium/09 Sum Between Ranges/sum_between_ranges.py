# sum_between_ranges.py
"""Assuming you have two integers, x and y, with y bigger than x. Sum all the numbers from x to y inclusively. Example: 
if x is 1 and y is 5, then sum 1+2+3+4+5."""


# imperatively
def sbr_imp(x, y):
    total = 0
    for n in range(x, y + 1):
        total += n
    return total


# using reduce and lambda
def sbr_reduce(x, y):
    from functools import reduce

    return reduce(lambda n, m: n + m, range(x, y + 1))


# using sum()
def sbr_sum(x, y):
    return sum([n for n in range(x, y + 1)])


if __name__ == "__main__":
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

    print("Imperatively:")
    for i, test_case in enumerate(test_cases):
        res = sbr_imp(test_case[0], test_case[1])
        print([answers[i] == res], res)

    print("\nUsing Reduce and lambda:")
    for i, test_case in enumerate(test_cases):
        res = sbr_reduce(test_case[0], test_case[1])
        print([answers[i] == res], res)

    print("\nUsing sum():")
    for i, test_case in enumerate(test_cases):
        res = sbr_sum(test_case[0], test_case[1])
        print([answers[i] == res], res)