# Practical Worksheet 2: Working with Numeric Types
# fmt: off
"""
Slope of a line using two points it goes through:
  (y2 - y1) / (x2 - x1)

Distance between two points using Pythagoras' theorem:
  sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""

import math


"""1. Write a function circumference_of_circle() that asks the user for the radius of a circle, and then outputs its 
circumference. (Use the formula circumference = 2πr. For π, use math.pi from the math module.)"""
def circumference_of_circle():
    radius = eval(input("\nEnter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print("The circumference is:", circumference)


"""2. Write a function area_of_circle() that asks the user for the radius of a circle, and then outputs its area (using 
the formula area = πr2)."""
def area_of_circle():
    radius = eval(input("\nEnter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area is:", area)


"""3. Write a function cost_of_pizza() that asks the user for the diameter (not the radius) of a pizza (in cm), and then 
outputs the cost of the pizza’s ingredients (based on its area) in pence. Assume that the cost of the ingredients is 
1.5p per square cm."""
def cost_of_pizza():
    diameter = eval(input("\nEnter the diameter of the pizza in centimetres: "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    print("The cost of the ingredients is", round(area * 1.5), "pence")


"""4. Write a function slope_of_line() that first asks the user for four values x1, y1, x2, and y2 that represent two 
points in two-dimensional space (i.e. points with coordinates (x1, y1) and (x2, y2)). The function should then output 
the slope of the line that connects them."""
def slope_of_line():
    x1 = eval(input("\nEnter the first x value: "))
    y1 = eval(input("Enter the first y value: "))
    x2 = eval(input("Enter the second x value: "))
    y2 = eval(input("Enter the second y value: "))

    slope = (y2 - y1) / (x2 - x1)
    print("Slope is:", slope)


"""5. Write a function distance_between_points() that asks the user for four values x1, y1, x2, and y2 that represent 
two points in two-dimensional space, and then outputs the distance between them."""
def distance_between_points():
    x1 = eval(input("\nEnter the first x value: "))
    y1 = eval(input("Enter the first y value: "))
    x2 = eval(input("Enter the second x value: "))
    y2 = eval(input("Enter the second y value: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Distance is:", distance)


"""6. Write a function travel_statistics() which asks the user to input the average speed (in km/hour) and duration (in 
hours) of a car journey. The function should then output the overall distance travelled (in km), and the amount of fuel 
used (in litres) assuming a fuel efficiency of 5 km/litre."""
def travel_statistics():
    avg_speed = eval(input("\nEnter your average speed in km/hour: "))
    duration = eval(input("Enter the duration of the car journey in hours: "))

    distance = avg_speed * duration
    print("You travelled a total of", distance, "km")

    fuel_consumed = distance / 5
    print("You used roughly", fuel_consumed, "litres of fuel")


"""7. Write a function sum_of_numbers() that outputs the sum of the first n positive integers, where n is provided by 
the user. For example, if the user enters 4, the function should output 10 (i.e. 1 + 2 + 3 + 4). (Hint: This function 
should use a loop.)"""
def sum_of_numbers():
    try:
        n = int(input("\nEnter a number larger than 0: "))
        if n <= 0:
            print("Must be more than 0!")
    except:
        print("Invalid input!")

    total = 0
    while n > 0:
        total += n
        n -= 1
    print(total)


"""8. [harder] Write a function average_of_numbers() which outputs the average of a series of numbers entered by the 
user. The function should first ask the user how many numbers there are to be inputted."""
def average_of_numbers():
    while True:
        try:
            no_of_inputs = int(input("\nEnter how many numbers you want to input: "))
            if no_of_inputs <= 1:
                print("Must be more than 1!")
            else:
                break
        except:
            print("Invalid input!")

    sum_of_inputs = 0
    for _ in range(no_of_inputs):
        while True:
            try:
                n = int(input("\nEnter a whole number: "))
                if n <= 0:
                    print("Must be more than 0!")
                else:
                    break
            except:
                print("Invalid input!")
        sum_of_inputs += n
    print("The average of these numbers is", sum_of_inputs / no_of_inputs)


"""9. [harder] Write a function select_coins() that asks the user to enter an amount of money (in pence) and then 
outputs the number of coins of each denomination (from £2 down to 1p) that should be used to make up that amount exactly 
(using the least possible number of coins). For example, if the input is 292, then the function should report: 1 × £2, 
0 × £1, 1 × 50p, 2 × 20p, 0 × 10p, 0 × 5p, 1 × 2p, 0 × 1p. (Hint: use integer division and remainder)."""
def select_coins():
    pence = int(input("\nEnter an amount in pence: "))

    two_pound = pence // 200
    pence = pence % 200
    print(two_pound, "x £2")

    one_pound = pence // 100
    pence = pence % 100
    print(one_pound, "x £1")

    fifty_pence = pence // 50
    pence = pence % 50
    print(fifty_pence, "x 50p")

    twenty_pence = pence // 20
    pence = pence % 20
    print(twenty_pence, "x 20p")

    ten_pence = pence // 10
    pence = pence % 10
    print(ten_pence, "x 10p")

    five_pence = pence // 5
    pence = pence % 5
    print(five_pence, "x 5p")

    two_pence = pence // 2
    pence = pence % 2
    print(two_pence, "x 2p")

    print(pence, "x 1p")


if __name__ == "__main__":
    functions = [
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
