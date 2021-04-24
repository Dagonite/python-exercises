# Practical Worksheet 2: Working with Numeric Types
"""
Slope of a line using two points it goes through:
• (y2 - y1) / (x2 - x1)

Distance between two points using Pythagoras' theorem:
• sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""

import math


def circumference_of_circle():
    """
    1. Write a function, circumference_of_circle(), that asks the user for the radius of a circle, and then outputs its
    circumference using the formula circumference = 2πr. For π, use math.pi from the math module.
    """
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print("The circumference is", circumference)


def area_of_circle():
    """
    2. Write a function, area_of_circle(), that asks the user for the radius of a circle, and then outputs its area
    using the formula area = πr2.
    """
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area is", area)


def cost_of_pizza():
    """
    3. Write a function cost_of_pizza() that asks the user for the diameter (not the radius) of a pizza (in cm), and
    then outputs the cost of the pizza’s ingredients (based on its area) in pence. Assume that the cost of the
    ingredients is 1.5p per square cm.
    """
    diameter = float(input("Enter the diameter of the pizza in centimetres: "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    print("The cost of the ingredients is", round(area * 1.5), "pence")


def slope_of_line():
    """
    4. Write a function, slope_of_line(), that first asks the user for four values x1, y1, x2, and y2 that represent two
    points in two-dimensional space (i.e. points with coordinates (x1, y1) and (x2, y2)). The function should then
    output the slope of the line that connects them.
    """
    x1 = float(input("Enter the first x value: "))
    y1 = float(input("Enter the first y value: "))
    x2 = float(input("Enter the second x value: "))
    y2 = float(input("Enter the second y value: "))

    slope = (y2 - y1) / (x2 - x1)
    print("The slope is", slope)


def distance_between_points():
    """
    5. Write a function, distance_between_points(), that asks the user for four values x1, y1, x2, and y2 that represent
    two points in two-dimensional space, and then outputs the distance between them.
    """
    x1 = float(input("Enter the first x value: "))
    y1 = float(input("Enter the first y value: "))
    x2 = float(input("Enter the second x value: "))
    y2 = float(input("Enter the second y value: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The distance is", distance)


def travel_statistics():
    """
    6. Write a function, travel_statistics(), which asks the user to input the average speed (in km/hour) and duration
    (in hours) of a car journey. The function should then output the overall distance travelled (in km), and the amount
    of fuel used (in litres) assuming a fuel efficiency of 5 km/litre.
    """
    avg_speed = float(input("Enter your average speed in km/hour: "))
    duration = float(input("Enter the duration of the car journey in hours: "))

    distance = avg_speed * duration
    print("You travelled a total of", distance, "km")

    fuel_consumed = distance / 5
    print("You used roughly", fuel_consumed, "litres of fuel")


def sum_of_numbers():
    """
    7. Write a function, sum_of_numbers(), that outputs the sum of the first n positive integers, where n is provided by
    the user. For example, if the user enters 4, the function should output 10 (i.e. 1 + 2 + 3 + 4). Hint: this function
    should use a loop.
    """
    while True:
        n = int(input("Enter a number larger than 0: "))

        if n <= 0:
            print("Must be more than 0!\n")
        else:
            break

    sequence = " + ".join(map(str, range(1, n + 1)))
    print(sequence, "=", eval(sequence))


def average_of_numbers():
    """
    8. [harder] Write a function, average_of_numbers(), which outputs the average of a series of numbers entered by the
    user. The function should first ask the user how many numbers there are to be inputted.
    """
    while True:
        no_of_inputs = int(input("Enter how many numbers you want to input: "))

        if no_of_inputs <= 1:
            print("Must be more than 1!\n")
        else:
            break

    print()

    sum_of_inputs = 0
    for _ in range(no_of_inputs):
        while True:
            n = float(input("Enter a whole number: "))

            if n <= 0:
                print("Must be more than 0!\n")
            else:
                break
        sum_of_inputs += n

    print("The average of these numbers is", sum_of_inputs / no_of_inputs)


def select_coins():
    """
    9. [harder] Write a function select_coins() that asks the user to enter an amount of money (in pence) and then
    outputs the number of coins of each denomination (from £2 down to 1p) that should be used to make up that amount
    exactly (using the least possible number of coins). For example, if the input is 292, then the function should
    report: 1 × £2, 0 × £1, 1 × 50p, 2 × 20p, 0 × 10p, 0 × 5p, 1 × 2p, 0 × 1p. Hint: use integer division and remainder.
    """
    pence = int(input("Enter an amount in pence: "))

    COINS = {
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20,
        "10p": 10,
        "5p": 5,
        "2p": 2,
        "1p": 1,
    }

    for coin, coin_value in COINS.items():
        no_of_coin = pence // coin_value
        pence = pence % coin_value
        print(no_of_coin, "x", coin)


if __name__ == "__main__":
    funcs = [
        circumference_of_circle,
        area_of_circle,
        cost_of_pizza,
        slope_of_line,
        distance_between_points,
        travel_statistics,
        sum_of_numbers,
        average_of_numbers,
        select_coins,
    ]

    no_of_funcs = len(funcs)
    print("".join(func.__doc__ for func in funcs))

    while True:
        try:
            func_number = int(input("\nEnter the number of the function to demo (0 to quit): "))

            if func_number == 0:
                print("Goodbye!")
                break
            elif 0 < func_number <= no_of_funcs:
                print()
                funcs[func_number - 1]()
            else:
                raise ValueError
        except:
            print("Invalid input")
