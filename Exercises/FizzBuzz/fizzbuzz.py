# fizzbuzz.py
"""Write a function that prints out FizzBuzz (1 - 100) up to range."""


def fizzbuzz(x):
    for n in range(1, x + 1):
        output = ""

        if n % 3 == 0:
            output = "Fizz"

        if n % 5 == 0:
            output += "Buzz"

        print(output or n)


fizzbuzz(100)
