"""Practical Worksheet 1: Getting started with Python"""

import os
from inspect import cleandoc


def say_name():
    """1. Write a function, say_name(), that displays your name."""
    print("John Doe")


def say_hello_world():
    """
    2. Write a function, say_hello_world(), that uses two print statements to
    display 'Hello world'.
    """
    print("Hello")
    print("world")


def euros_to_pounds():
    """
    3. Write a function, euros_to_pounds(), that converts an amount in Euros
    entered by the user to a corresponding amount in Pounds. Assume that the
    exchange rate is 1.108 Euros to the Pound.
    """
    euros = float(input("Enter an amount in euros: "))
    pounds = euros / 1.108
    print(f"The amount in pounds is {pounds:.2f}")


def add_up():
    """
    4. Write a function, add_up(), that asks the user to enter two numbers and
    outputs the sum.
    """
    n = float(input("Gimme a number: "))
    m = float(input("Gimme another number: "))
    total = n + m
    print("The sum is", total)


def change_counter():
    """
    5. Write a function, change_counter(), that asks the user how many 1p, 2p,
    and 5p coins they have (using three separate questions), and then display
    the total amount of money in pence.

    Hint: remember that variable names cannot begin with a digit, so you might
    like to use names like 'two_pence'.
    """
    one_pence = int(input("How many 1p coins do you have? "))
    two_pence = int(input("How many 2p coins do you have? "))
    five_pence = int(input("How many 5p coins do you have? "))
    total_pence = one_pence + two_pence * 2 + five_pence * 5
    print("The sum of your coins is", total_pence, "pence")


def ten_hellos():
    """
    6. Write a function, ten_hellos(), that uses a loop to display 'Hello world'
    ten times (on separate lines).
    """
    for _ in range(10):
        print("Hello world")


def count():
    """
    7. Write a function, count(), that instead of counting from 0 to 9, it
    counts up from 1 to 10.

    Hint: use a little arithmetic in the print statement.
    """
    for i in range(10):  # in reality this is dumb, you would just do range(1, 11)
        print(i + 1)


def weights_table():
    """
    8. [harder] Write a function, weights_table(), that outputs a two-column
    table of kilogram weights and their pound equivalents for kilogram values 0,
    10, 20, ..., 100. Don't worry too much about formatting the table neatly.
    """
    for i in range(11):
        print(i * 10, i * 22)


def future_value():
    """
    9. [harder] Write a function, future_value(), that uses a loop to calculate
    the future value of an investment amount, assuming an annual interest rate
    of 5.5%. The function should ask the user for the initial amount and the
    number of years that it is to be invested, and should output the final value
    of the investment using compound interest with the interest compounded every
    year.
    """
    investment = float(input("Enter the investment amount in GBP: "))
    years = int(input("Enter the years of investment: "))
    interest_rate = 0.055
    return_amount = investment
    for _ in range(years):
        return_amount *= 1 + interest_rate
    print(f"Investing £{investment:.2f} for {years} years will result in £{return_amount:.2f}")


def main():
    funcs = [
        say_name,
        say_hello_world,
        euros_to_pounds,
        add_up,
        change_counter,
        ten_hellos,
        count,
        weights_table,
        future_value,
    ]
    func_count = len(funcs)

    def print_func_names():
        """Prints the index and name of all of the functions in this script."""
        print("\nFunctions:")
        for i, func in enumerate(funcs, start=1):
            print(f"{i} {func.__name__}")

    print_func_names()

    while True:
        try:
            ans = int(input("\nEnter the number of the function to demo (0 to quit) > "))
            if ans == 0:
                print("Goodbye!")
                break
            if 0 < ans <= func_count:
                os.system("cls" if os.name == "nt" else "clear")
                func = funcs[ans - 1]
                print(f"{'=' * 76}\n{cleandoc(func.__doc__)}\n{'=' * 76}\n")
                func()
                print_func_names()
            else:
                raise ValueError("invalid: no such demo exists")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
