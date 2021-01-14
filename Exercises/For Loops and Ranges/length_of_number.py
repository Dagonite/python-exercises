# length_of_number.py
"""Create a function that takes a number and returns its length without using the len function."""


def number_length(num):
    return sum(1 for _ in str(num))


print(number_length(5))
print(number_length(12))
print(number_length(402))
print(number_length(1230))
print(number_length(63464))
print(number_length(123532))