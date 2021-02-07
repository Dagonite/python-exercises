# validate_pin.py
"""Create a function to test if a string is a valid pin or not. A valid pin has:
-Exactly 4 or 6 characters
-Only numerical characters (0-9)
-No whitespace
"""


def valid(txt):
    return txt.isnumeric() and len(txt) in [4, 6]


print(valid("1422"))
print(valid("abcd"))
print(valid("14ab"))
print(valid("14225"))
print(valid("ab14c"))
print(valid("abcde"))
print(valid("234133"))
print(valid("abcdef"))
print(valid("14ab15"))