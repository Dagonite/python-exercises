# one_line_fizzbuzz.py
"""Write a function that returns FizzBuzz as a list."""


def fizzbuzz(x):
    return ["Fizz" * (n % 3 < 1) + "Buzz" * (n % 5 < 1) or n for n in range(1, x + 1)]


print(fizzbuzz(100))
