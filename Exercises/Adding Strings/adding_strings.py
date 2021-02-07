# adding_numbers.py
"""Create a function that takes two number strings and returns their sum as a string. If any input is "" or None, return 
"Invalid Operation"."""


def add(a, b):
    try:
        return str(int(a) + int(b))
    except:
        return "Invalid Operation"


print(add("5", "5"))
print(add("-5", "6"))
print(add("-3", "-3"))
print(add("", None))
print(add(None, None))
print(add("", ""))
