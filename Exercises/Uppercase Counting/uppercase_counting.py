# uppercase_counting.py
"""Write a function which returns how many uppercase letters there are in a list of various words."""


def count_uppercase(lst):
    return sum(letter.isupper() for word in lst for letter in word)


print(count_uppercase(["BIG head", "cAmEl HuMps", "COOL", "meh"]))
