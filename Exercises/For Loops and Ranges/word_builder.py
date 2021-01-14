# word_builder.py
"""Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to 
establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the 
word)."""


def word_builder(ltr, pos):
    return "".join(ltr[i] for i in pos)


print(word_builder(["r", "e", "d", "a"], [2, 1, 3, 0]))
print(word_builder(["g", "e", "u", "s", "i", "n"], [0, 1, 5, 4, 2, 3]))
print(word_builder(["d", "u", "i", "q", "i", "l"], [5, 4, 3, 2, 1, 0]))
