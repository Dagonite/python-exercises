"""Write a function that takes in a positive integer and returns its multiplicative persistence, which is the number of 
times you must multiply the digits in the integer until you reach a single digit. For example the integer 39 returns 3. 
You get this by taking 39 and multiplying its digits 3*9 which equals 27. You then multiply 27's digits, 2*7 = 14. 
Lastly, 1*4 = 4 which is a single digit. You had to multiply 3 times so you return 3. The integer 999 would return 4."""


def multiplicative_persistence(n):
    from functools import reduce

    sum_n = n
    no_of_splits = 0
    while True:
        if sum_n < 10:
            break
        split_n = list(str(sum_n))
        sum_n = reduce(lambda x, y: int(x) * int(y), split_n)
        no_of_splits += 1
    return no_of_splits


if __name__ == "__main__":
    test_cases = [
        55,
        22,
        8,
        999,
        1246,
        838324,
        6788,
    ]

    answers = [
        3,
        1,
        0,
        4,
        3,
        2,
        6,
    ]

    for i, test_case in enumerate(test_cases):
        res = multiplicative_persistence(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)