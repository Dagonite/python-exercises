# way_too_long_words.py
"""Write a program that takes a specified number of words, converting each one if its length is strictly more than 10 
characters. These long words will be replaced with a string starting with the first character of the word and ending 
with the last character of the word. Inbwetween will be the number of letters that make up the rest of the word."""

for _ in [0] * int(input("Enter the number of words to convert: ")):
    word = input("Enter a word: ")
    length = len(word) - 2
    print([word, word[0] + str(length) + word[-1]][length > 8])
