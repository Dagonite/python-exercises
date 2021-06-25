"""In each input list, every number repeats at least once, except for two. Write a function that returns the two unique 
numbers."""


def return_unique(lst):
    return [n for n in lst if lst.count(n) == 1]


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 1, 2, 3],
        [1, 1, 1, 2, 2, 2, 3, 4],
        [1, 2, 2, 3, 4, 4, 5, 5],
    ]

    answers = [
        [4, 5],
        [3, 4],
        [1, 3],
    ]

    for i, test_case in enumerate(test_cases):
        res = return_unique(test_case)
        print([answers[i] == res], res)