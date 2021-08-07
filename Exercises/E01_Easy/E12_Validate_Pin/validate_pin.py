"""
Create a function to test if a string is a valid pin or not. A valid pin has 
exactly 4 or 6 characters, only numerical characters (0-9), and no whitespace.
"""


def valid(txt):
    return txt.isnumeric() and len(txt) in [4, 6]


if __name__ == "__main__":
    test_cases = [
        "1422",
        "abcd",
        "14ab",
        "ab14c",
        "14225",
        "abcde",
        "234133",
        "abcdef",
        "14ab15",
        " 232",
        " 92 ",
        "123 ",
        "9834 ",
    ]

    answers = [
        True,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
    ]

    for i, test_case in enumerate(test_cases):
        res = valid(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", f"{test_case} = {res}")
