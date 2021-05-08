# max_length.py
"""Write a function that finds the maximum length of a concatenated string with unique characters."""


def max_length(arr):
    dp = [set()]
    for word in arr:
        if len(set(word)) < len(word):
            continue
        word = set(word)
        for next_word in dp[:]:
            if word & next_word:
                continue
            dp.append(word | next_word)
    return max(len(word) for word in dp)


if __name__ == "__main__":
    test_cases = [
        ["at", "ee", "tude", "blou"],
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"],
        ["b", "b"],
        [],
        ["att", "itude", "gril"],
        ["a", "b", "c", "d", "d", "d"],
    ]

    answers = [
        6,
        11,
        1,
        0,
        5,
        4,
    ]

    for i, test_case in enumerate(test_cases):
        res = max_length(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)