"""
Write a function that sorts a given string. Each word in the string will contain
a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
string will only contain valid consecutive numbers.
"""


def order(words):
    return " ".join(sorted(words.split(), key=sorted))


if __name__ == "__main__":
    test_cases = [
        "is2 Thi1s T4est 3a",
        "4of Fo1r pe6ople g3ood th5e the2",
        "d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6",
    ]

    answers = [
        "Thi1s is2 3a T4est",
        "Fo1r the2 g3ood 4of th5e pe6ople",
        "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor",
    ]

    for i, test_case in enumerate(test_cases):
        res = order(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
