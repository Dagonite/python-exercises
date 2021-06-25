"""Create a function that returns the number of characters shared between two words."""


def shared_letters(str1, str2):
    return len(set(str1) & set(str2))


if __name__ == "__main__":
    test_cases = [
        ("blue", "red"),
        ("spout", "shout"),
        ("familiar", "friend"),
    ]

    answers = [
        1,
        4,
        3,
    ]

    for i, test_case in enumerate(test_cases):
        res = shared_letters(test_case[0], test_case[1])
        print("[Pass]" if answers[i] == res else "[Fail]", res)