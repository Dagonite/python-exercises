"""
Create a function that takes two number strings and returns their sum as a 
string. If any input is '' or None, return 'Invalid Operation'.
"""


def add(a, b):
    try:
        return str(int(a) + int(b))
    except ValueError:
        return "invalid operation"


if __name__ == "__main__":
    test_cases = [
        ("5", "5"),
        ("-5", "6"),
        ("-3", "-3"),
        ("", "None"),
        ("None", "None"),
        ("", ""),
    ]

    answers = [
        "10",
        "1",
        "-6",
        "invalid operation",
        "invalid operation",
        "invalid operation",
    ]

    for i, test_case in enumerate(test_cases):
        res = add(test_case[0], test_case[1])
        print([answers[i] == res], res)
