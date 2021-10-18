"""
Write a function that takes a string containing 3 numbers: A, B, and N. The
function should print integers 1 to N but for integers that are multiples of A,
print 'F' and for multiples of B, print 'B'. For multiples of both A and B,
print 'FB'.
"""


def fizzbuzz(line):
    fizz, buzz, n = map(int, line.split())
    return " ".join("F" * (i % fizz == 0) + "B" * (i % buzz == 0) or str(i) for i in range(1, n + 1))


if __name__ == "__main__":
    test_cases = [
        "3 5 10",
        "2 7 15",
        "5 6 30",
    ]

    answers = [
        "1 2 F 4 B F 7 8 F B",
        "1 F 3 F 5 F B F 9 F 11 F 13 FB 15",
        "1 2 3 4 F B 7 8 9 F 11 B 13 14 F 16 17 B 19 F 21 22 23 B F 26 27 28 29 FB",
    ]

    for i, test_case in enumerate(test_cases):
        res = fizzbuzz(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
