# odd_occurrence.py
"""Given a list of numbers, write a function to find the number in the list that appears an odd number of times."""

from functools import reduce
from collections import Counter


def find_odd_occurrence_1(seq):
    """Solution using the Counter class."""
    counts = Counter(seq)
    for n in counts:
        if counts[n] % 2:
            return n


def find_odd_occurrence_2(seq):
    """Solution using the xor operator and reduce(). Exclusive or is commutative, which results in an odd occurence of a
    number in a sequence not being cancelled out when being reduced. Problem with reduce() is that there's quite a bit
    overhead as the lambda func is getting called for every element in the sequence."""
    return reduce(lambda x, y: x ^ y, seq)


def find_odd_occurrence_3(seq):
    """Similar solution to 2 except using a for loop instead of reduce(). This way is much faster."""
    x = 0
    for n in seq:
        x ^= n
    return x


if __name__ == "__main__":
    from random import randrange, shuffle
    from timing import timed_func  # timing can be found in my python-sorting-algorithms repo

    solutions = [
        find_odd_occurrence_1,
        find_odd_occurrence_2,
        find_odd_occurrence_3,
    ]

    test_cases = []
    for i in range(5):
        list_1 = [randrange(1, 10) for _ in range(8000)]
        list_2 = list_1[:]
        n = randrange(1, 10)
        list_3 = [n] * randrange(1, 6, 2)
        seq = list_1 + list_2 + list_3
        shuffle(seq)
        test_cases.append(seq)

    for solution in solutions:
        print(f"{solution.__name__}:")
        solution = timed_func(solution)
        for test_case in test_cases:
            res, seconds = solution(test_case)
            print(f"{res}, that took {seconds}s")
        print()
