# is_palindrome_list_comprehension.py
"""Checks if a string is a palindrome. This solution requires linear time and linear space so isn't the most efficient, 
however is very concise."""

in_file = open("palindromes.txt", "r")
lines = in_file.readlines()
in_file.close()

for line in lines:
    s = "".join([ch for ch in line if ch.isalnum()]).replace(" ", "").lower()
    print("{:<34}{}".format(line[:-1], s == s[::-1]))
