"""Write a function that returns FizzBuzz values 1 to 100 as a list."""


def fizzbuzz():
    return ["Fizz" * (n % 3 < 1) + "Buzz" * (n % 5 < 1) or n for n in range(1, 101)]


print(fizzbuzz())
