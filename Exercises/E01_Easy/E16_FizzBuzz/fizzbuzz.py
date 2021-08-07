"""Write a function that prints out FizzBuzz values 1 to 100."""


def fizzbuzz():
    for n in range(1, 101):
        output = ""

        if n % 3 == 0:
            output = "Fizz"

        if n % 5 == 0:
            output += "Buzz"

        print(output or n)


fizzbuzz()
