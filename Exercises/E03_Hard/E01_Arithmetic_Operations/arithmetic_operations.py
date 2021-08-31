"""
Create a function to perform basic arithmetic operations (addition, subtraction, 
multiplication, and division) on a string equation (e.g, "12 + 24" should return 
36).
"""

from operator import add, sub, floordiv, mul


def arithmetic_operation(equation):
    OPS = {"+": add, "-": sub, "*": mul, "//": floordiv}
    a, op, b = equation.split()

    try:
        return OPS[op](int(a), int(b))
    except ZeroDivisionError:
        return -1


if __name__ == "__main__":
    test_cases = [
        "11 + 10",
        "8 - 4",
        "6 * 7",
        "24 // 8",
        "5 // 0",
    ]

    answers = [
        21,
        4,
        42,
        3,
        -1,
    ]

    for i, test_case in enumerate(test_cases):
        res = arithmetic_operation(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
