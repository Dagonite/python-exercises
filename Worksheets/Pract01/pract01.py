# Practical Worksheet 1: Getting started with Python
# fmt: off


"""1. Write a function called say_name() that displays your name."""
def say_name():
    print("\nJohn Doe")


"""2. Write a say_hello_world() function that uses two print statements to display the text."""
def say_hello_world():
    print("\nHello")
    print("World")


"""3. Write a function euros_to_pounds() which converts an amount in Euros entered by the user to a corresponding amount 
in Pounds. Assume that the exchange rate is 1.15 Euros to the Pound."""
def euros_to_pounds():
    euros = eval(input("\nEnter an amount in euros: "))
    pounds = euros / 1.108
    print(f"The amount in pounds is {pounds:.2f}")


"""4. Write an add_up() function that asks the user to enter two numbers, and outputs their sum."""
def add_up():
    n = eval(input("\nGimme a number: "))
    m = eval(input("Gimme another number: "))
    total = n + m
    print("The sum of them is", total)


"""5. Write a change_counter() function. This should ask the user how many 1p, 2p and 5p coins they have (using three 
separate questions), and then display the total amount of money in pence. (Hint: remember that variable names cannot 
begin with a digit, so you might like to use names like two_pence.)"""
def change_counter():
    one_pence = eval(input("\nHow many 1p coins do you have? "))
    two_pence = eval(input("How many 2p coins do you have? "))
    five_pence = eval(input("How many 5p coins do you have? "))
    total_pence = one_pence + two_pence * 2 + five_pence * 5
    print("The sum of your coins is", total_pence, "pence")


"""6. Write a ten_hellos() function that uses a loop to display “hello, world!” ten times (on separate lines)."""
def ten_hellos():
    print()
    for _ in range(10):
        print("hello, world")


"""7. Write a count() function so that instead of counting from 0 to 9, it counts up from 1 to 10. (Hint: use a little 
arithmetic in the print statement.)"""
def count():
    print()
    for i in range(10):
        print(i + 1)


"""8. [harder] Write a function weights_table() that outputs a two-column table of kilogram weights and their pound 
equivalents for kilogram values 0, 10, 20 ... 100. (Don’t worry too much about formatting the table neatly.)"""
def weights_table():
    print()
    for i in range(11):
        print(i * 10, i * 22)


"""9. [harder] Write a future_value() function that uses a loop to calculate the future value of an investment amount, 
assuming an annual interest rate of 5.5%. The function should ask the user for the initial amount and the number of 
years that it is to be invested, and should output the final value of the investment using compound interest with the 
interest compounded every year."""
def future_value():
    investment = eval(input("\nEnter the investment amount in GBP: "))
    years = eval(input("Enter the years of investment: "))
    interest_rate = 0.055
    return_amount = investment
    for _ in range(years):
        return_amount *= 1 + interest_rate
    print(f"Investing £{investment:.2f} for {years} years will result in £{return_amount:.2f}")


if __name__ == "__main__":
    functions = [
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

    no_of_functions = len(functions)

    while True:
        try:
            f_number = int(input("\nEnter the question number you would like to demo (0 to quit): "))
            if f_number == 0:
                break
            elif f_number < 0 or f_number > no_of_functions:
                print("Answer out of range!")
            else:
                function = functions[f_number - 1]
                function()
        except:
            print("Invalid input!")