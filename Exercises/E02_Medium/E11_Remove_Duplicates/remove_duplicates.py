"""
Create a function which takes a list of numbers and returns a list with 
duplicates removed without affecting the order of the list.
"""


def remove_duplicates(data):
    unique_data = set()
    unique_data_add = unique_data.add
    return [i for i in data if not (i in unique_data or unique_data_add(i))]


if __name__ == "__main__":
    test_cases = [
        [7, 6, 4, 3, 3, 4, 9],
        [6],
        [1, 1, 3, 9, 3, 9, 8, 8],
        [3, 1, 1, 1, 3, 1, 2],
    ]

    answers = [
        [7, 6, 4, 3, 9],
        [6],
        [1, 3, 9, 8],
        [3, 1, 2],
    ]

    for i, test_case in enumerate(test_cases):
        res = remove_duplicates(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
