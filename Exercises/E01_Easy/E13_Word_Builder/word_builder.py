"""Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to 
establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the 
word)."""


def word_builder(ltr, pos):
    return "".join(ltr[i] for i in pos)


if __name__ == "__main__":
    test_cases = [
        (["r", "e", "d", "a"], [2, 1, 3, 0]),
        (["g", "e", "u", "s", "i", "n"], [0, 1, 5, 4, 2, 3]),
        (["d", "u", "i", "q", "i", "l"], [5, 4, 3, 2, 1, 0]),
    ]

    answers = [
        "dear",
        "genius",
        "liqiud",
    ]

    for i, test_case in enumerate(test_cases):
        res = word_builder(test_case[0], test_case[1])
        print("[Pass]" if answers[i] == res else "[Fail]", res)