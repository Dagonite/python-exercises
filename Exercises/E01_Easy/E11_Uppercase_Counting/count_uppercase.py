"""Write a function which returns how many uppercase letters there are in a list of various words."""


def count_uppercase(lst):
    return sum(letter.isupper() for word in lst for letter in word)


if __name__ == "__main__":
    test_cases = [
        ["BIG head", "cAmEl HuMps", "COOL", "meh"],
        ["larGE", "letteRS", "heRE"],
    ]

    answers = [
        11,
        6,
    ]

    for i, test_case in enumerate(test_cases):
        res = count_uppercase(test_case)
        print([answers[i] == res], res)