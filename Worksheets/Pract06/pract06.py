"""Practical Worksheet 6: If Statements and For Loops"""

import random

from graphics import Circle, GraphWin, Line, Point, Polygon, Rectangle, Text

from pract05 import distance_between_points


def fast_food_order_price():
    """
    1. A fast-food company charges £1.50 for delivery to your home, except for
    large orders of £10 or more where delivery is free. Write a function,
    fast_food_order_price(), that asks the user for the basic price of an order
    and prints a 'The total price of your order is ...' message containing the
    total price including any delivery charges.
    """
    price = float(input("Enter the price of the food order > "))
    if price < 10:
        price += 1.50
    print("The total price of your order is £{:.2f}".format(price))


def what_to_do_today():
    """
    2. Write a what_to_do_today() function that asks the user to enter today's
    temperature, and then prints a message suggesting what to do. For
    temperatures of above 25 degrees, a swim in the sea should be suggested; for
    temperatures between 10 and 25 degrees (inclusive), shopping in Gunwharf
    Quays is a good idea, and for temperatures of below 10 degrees it's best to
    watch a film at home.
    """
    temperature = int(input("Enter the temperature > "))
    if temperature > 25:
        print("Go swim in the sea")
    elif temperature >= 10 and temperature <= 25:
        print("Go shopping in Gunwharf Quays")
    else:
        print("Watch a film at home")


def display_square_roots(start=None, end=None):
    """
    3. Write a function display_square_roots() that has two parameters, start
    and end, and displays the square roots of numbers between these two values,
    shown to three decimal places. For example, the call
    display_square_roots(2, 4) should result in the following output:

    'The square root of 2 is 1.414'
    'The square root of 3 is 1.732'
    'The square root of 4 is 2.000'
    """
    if start is None or end is None:
        start = int(input("Enter a number > "))
        end = int(input("Enter a number larger than the previous > "))

    for i in range(start, end + 1):
        print("The square root of {} is {:.3f}".format(i, i ** 0.5))


def calculate_grade(mark=None):
    """
    4. A school teacher marks her pupils' coursework out of 20, but needs to
    translate these marks to a grade of A, B, C, or F (where marks of 16 or
    above get an A, marks between 12 and 15 result in a B, marks between 8 and
    11 give a C, and marks below 8 get an F). Write a calculate_grade() function
    that takes a mark as a parameter and returns the corresponding grade as a
    single-letter string. If the parameter value is too big or too small, the
    function should return a mark of X.
    """
    if mark is None:
        mark = int(input("Enter a mark > "))

    if mark > 20 or mark < 0:
        return "X"
    elif mark >= 16:
        return "A"
    elif mark >= 12:
        return "B"
    elif mark >= 8:
        return "C"
    else:
        return "F"


def peas_in_a_pod():
    """
    5. Write a function peas_in_a_pod() that asks the user for a number, and
    then draws that number of 'peas' (green circles of radius 50) in a 'pod'
    (graphics window of exactly the right size). E.g. if the user enters 5, a
    graphics window of size 500 × 100 should appear.
    """
    peas = int(input("Enter a number of peas: "))
    win = GraphWin("Peas in a pod", peas * 100, 100)
    for pea in range(peas):
        circle = Circle(Point(50 + pea * 100, 50), 50)
        circle.setFill("green")
        circle.draw(win)

    win.getMouse()
    win.close()


def ticket_price(distance=None, age=None):
    """
    6. A train company prices tickets based on journey distance: tickets cost £3
    plus 15p for each kilometre (e.g. a ticket for a 100 kilometre journey costs
    £18). However, senior citizens (people who are 60 or over) and children (15
    or under) get a 40% discount. Write a ticket_price() function that takes the
    journey distance and passenger age as parameters (both integers), and
    returns the price of the ticket in pounds (i.e. a float).
    """
    if distance is None or age is None:
        distance = float(input("Enter a distance > "))
        age = int(input("Enter a age > "))

    ticket = 3 + distance * 0.15
    if age >= 60 or age <= 15:
        ticket *= 0.40
    return format(ticket, ".2f")


def numbered_square(n=None):
    """
    7. Write a numbered_square() function that has a parameter n and displays a
    'numbered' square of size n. The call numbered_square(4) should result in
    the output:

    4 5 6 7
    3 4 5 6
    2 3 4 5
    1 2 3 4

    Note: the top-left number should always be n.
    """
    if n is None:
        n = int(input("Enter a number > "))

    for y in range(n, 0, -1):
        for x in range(n):
            print(x + y, end=" ")
        print()


def draw_circle(win, centre, radius, colour):
    """Helper function for drawing a circle."""
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def draw_coloured_eye(win, centre, radius, colour):
    """Helper function for drawing a coloured eye."""
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius / 2, colour)
    draw_circle(win, centre, radius / 4, "black")


def eye_picker():
    """
    8. The pract06.py file contains an incomplete draw_coloured_eye() function
    for which the graphics window, centre point, radius and eye colour (a
    string) are given as parameters. Complete the draw_coloured_eye() function
    so that it draws an eye like those from last week, but for any given colour.
    Write another function eye_picker() that asks the user for the coordinates
    of the centre of an eye, its radius and colour. If the user inputs a valid
    eye colour (blue, grey, green, or brown), then an appropriately coloured eye
    should be displayed in a graphics window. Otherwise, just a 'not a valid eye
    colour' message should be output. Remember to avoid repetitive code.
    """
    centre_coord = eval(input("Enter the coordinate for the centre of the eye (as a tuple) > "))
    x_coord, y_coord = centre_coord
    centre = Point(x_coord, y_coord)
    radius = float(input("Enter the radius of the eye > "))
    colours = ["grey", "green", "blue", "green"]
    print(*colours, sep=", ")

    while True:
        try:
            colour = input("Enter the colour of the eye > ").lower()
            if colour in colours:
                break
        except Exception:
            print("Not a valid eye colour")

    win = GraphWin("Coloured eye")
    draw_coloured_eye(win, centre, radius, colour)

    win.getMouse()
    win.close()


def draw_patch_window():
    """
    9. Write a function draw_patch_window() (without parameters) which displays, in
    a graphics window of size 100 × 100 pixels, the patch design which is
    labelled with the final digit of your student number. The patch design
    should be displayed in red, as in the table. It's important that your
    program draws the patch design accurately, but don't worry if one pixel is
    chopped off at the edge of the window. Note that you don't need to draw a
    border around the patch design.
    """
    win = GraphWin("Patch design", 100, 100)
    for distance in (20, 40, 60, 80, 100):
        line = Line(Point(0, distance), Point(distance, 0))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(100 - distance, 0), Point(100, distance))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

    for distance in (20, 40, 60, 80):
        line = Line(Point(distance, 100), Point(100, distance))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(0, distance), Point(100 - distance, 100))
        line.setFill("red")
        line.setWidth(2)
        line.draw(win)

    win.getMouse()
    win.close()


def draw_patch(win, x, y, colour):
    """Helper function for drawing a patch design."""
    for distance in (20, 40, 60, 80, 100):
        line = Line(Point(x, distance + y), Point(x + distance, y))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(x + 100 - distance, y), Point(x + 100, y + distance))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

    for distance in (20, 40, 60, 80):
        line = Line(Point(x + distance, y + 100), Point(x + 100, y + distance))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)

        line = Line(Point(x, y + distance), Point(x + 100 - distance, y + 100))
        line.setFill(colour)
        line.setWidth(2)
        line.draw(win)


def draw_patchwork():
    """
    10. Write a function draw_patch() which draws the same patch design, but
    which takes four parameters: the window in which to draw the patch, the x
    and y coordinates of where the top-left corner of the patch should be, and
    the colour of the patch.

    Write another function draw_patchwork() (without parameters) which uses
    draw_patch() to draw a blue 'patchwork' three patches wide and two patches
    high in a graphics window of size 300 x 200 pixels.
    """
    win = GraphWin("Patchwork", 300, 200)
    colour = "blue"
    for y in range(2):
        for x in range(3):
            draw_patch(win, x * 100, y * 100, colour)

    win.getMouse()
    win.close()


def eyes_all_around():
    """
    11. Write an eyes_all_around() function that allows the user to plot exactly
    30 eyes on a graphics window of dimensions 500 x 500 by clicking on chosen
    centre points. All eyes should be of radius 30, but they should be of
    different colours: specifically, the colours should repeatedly cycle through
    the sequence 'blue', 'grey', 'green' and 'brown'. Your function should call
    draw_coloured_eye() to draw each eye.
    """
    win = GraphWin("Eyes all around", 500, 500)
    colours = ["blue", "grey", "green", "brown"]
    for eye in range(30):
        eye_colour = eye % 4
        centre = win.getMouse()
        draw_coloured_eye(win, centre, 30, colours[eye_colour])

    win.getMouse()
    win.close()


# constants
GRADES = [
    "amazing at this game",
    "pretty good at this game",
    "average at this game",
    "below average at this game",
    "awful at this game",
]
WSD = 0.25  # wind start deviation
WD = 0.1  # wind deviation after an arrow is shot
WTH = 0.08  # wind threshold (determines wind direction threshold for the wind direction message)
ARROWS = 5  # number of arrows to shoot


def archery_game():
    """
    12. [harder] Write an archery_game() function. This function should draw a
    target (like that from pract03) using the supplied draw_circle() function.
    Your function should then allow the user to click on the graphics window
    five times, representing the firing of five arrows – each click representing
    the point on the target that is aimed at.

    Fluctuating atmospheric conditions should be considered – your solution
    should generate two random values representing the amount an arrow will move
    horizontally and vertically from the aimed position during its flight, and
    these values should be adjusted a little (again randomly) after each arrow.

    Generating random numbers is easily accomplished using the randint function
    from the random module. This function takes two arguments and returns a
    random number between these two values. For example, try:

    import random
    for i in range(10):
        print(random.randint(1, 5))

    Each time the user clicks, the function should:

    (i) display a small black circle representing where the arrow hits.
    (ii) record the number of points scored.

    The points awarded for each arrow (click) are as follows: 10 for the yellow
    area, 5 for red and 2 for blue. After the final arrow, the function should
    display the total score on the graphics window.

    Hint: calculate distances() by first importing your pract05.py file and
    using the distance_between_points() function.
    """

    win, wind_text, zone_text, score_text, score = draw_gui()
    score = shoot_arrows(win, wind_text, zone_text, score_text, score)
    give_grade(wind_text, score_text, score)

    # wait for user to click on the screen
    cursor = win.getMouse()
    cursor_x, cursor_y = cursor.getX(), cursor.getY()
    win.close()

    # if the user clicked on the target, reload the window
    if distance_between_points(Point(cursor_x, cursor_y), Point(0.5, 0.5)) <= 0.3:
        archery_game()


def draw_gui():
    """Helper function for creating the graphics window and drawing the target."""
    # create the window
    win = GraphWin("Archery game", 500, 500)
    win.setBackground("cyan")
    win.setCoords(0, 0, 1, 1)
    centre = Point(0.5, 0.5)

    # draw the grass
    ground_rect = Rectangle(Point(-0.01, -0.01), Point(1.01, 0.5)).draw(win)
    ground_rect.setFill("green")

    # draw the target legs
    left_target_stand = Polygon(Point(0.02, -0.01), Point(0.45, 0.5), Point(0.55, 0.5), Point(0.12, -0.01)).draw(win)
    left_target_stand.setFill("brown")
    left_target_stand.setWidth(2)

    right_target_stand = Polygon(Point(0.98, -0.01), Point(0.55, 0.5), Point(0.45, 0.5), Point(0.88, -0.01)).draw(win)
    right_target_stand.setFill("brown")
    right_target_stand.setWidth(2)

    # draw the target
    draw_circle(win, centre, 0.3, "blue")
    draw_circle(win, centre, 0.2, "red")
    draw_circle(win, centre, 0.1, "yellow")

    # draw the text displaying the score
    score = 0
    score_text = Text(Point(0.5, 0.04), f"Score: {score}").draw(win)
    score_text.setSize(18)
    score_text.setStyle("bold")

    # draw the text displaying where an arrow has landed
    zone_text = Text(Point(0.5, 0.09), "").draw(win)
    zone_text.setSize(12)
    zone_text.setStyle("bold")

    # draw the text describing wind conditions
    wind_text = Text(Point(0.5, 0.97), "Wind: ").draw(win)
    wind_text.setSize(12)
    wind_text.setStyle("bold")

    return win, wind_text, zone_text, score_text, score


def shoot_arrows(win, wind_text, zone_text, score_text, score):
    """Helper function that prompts the user to shoot arrows at the target by
    left-clicking.
    """
    h_wind, v_wind = random.uniform(-WSD, WSD), random.uniform(-WSD, WSD)

    for _ in range(ARROWS):
        # determine wind direction
        wind = ""
        if v_wind > WTH:
            wind += "north"
        elif v_wind < -WTH:
            wind += "south"
        if h_wind > WTH:
            wind += "east"
        elif h_wind < -WTH:
            wind += "west"
        if wind == "":
            wind = "Calm"

        # display wind direction
        wind_text.setText(f"Wind: {wind.title()}")

        # wait for left-click
        cursor_pos = win.getMouse()
        arrow_x = cursor_pos.getX() + h_wind  # add horizontal wind to x value
        arrow_y = cursor_pos.getY() + v_wind  # add vertical wind to y value

        # add wind deviation for next arrow shot
        h_wind += random.uniform(-WD, WD)
        v_wind += random.uniform(-WD, WD)

        # get the distance from the target centre of where the arrow will land
        arrow_zone = distance_between_points(Point(arrow_x, arrow_y), Point(0.5, 0.5))

        # determine what zone the arrow will land in
        if arrow_zone <= 0.3:
            draw_arrow(win, arrow_x, arrow_y)
            if arrow_zone < 0.1:
                zone_text.setText("YELLOW ZONE (10 POINTS!)")
                score += 10
            elif arrow_zone >= 0.1 and arrow_zone < 0.2:
                zone_text.setText("RED ZONE (5 POINTS!)")
                score += 5
            else:
                zone_text.setText("BLUE ZONE (2 POINTS!)")
                score += 2
        else:
            zone_text.setText("TARGET MISSED (0 POINTS!)")

        score_text.setText(f"Score: {score}")

    return score


def give_grade(wind_text, score_text, score):
    """Helper function for displaying what score and grade the user has
    received.
    """
    if score > 220 / ARROWS:
        grade = 0
    elif score > 170 / ARROWS:
        grade = 1
    elif score > 120 / ARROWS:
        grade = 2
    elif score > 95 / ARROWS:
        grade = 3
    else:
        grade = 4

    grade_text = GRADES[grade]
    wind_text.setText(f"You scored {score}, meaning you're {grade_text}")

    score_text.setSize(10)
    score_text.setText("Click on the target to play again\nClick anywhere else to quit")


def draw_arrow(win, arrow_x, arrow_y):
    """Helper function that draws an arrow onto the given graphics window."""
    arrow_shaft = Circle(Point(arrow_x, arrow_y), 0.008).draw(win)
    arrow_shaft.setFill("brown")

    for x in (1, -1):
        fletching = Line(Point(arrow_x + 0.02, arrow_y + 0.02 * x), Point(arrow_x - 0.02, arrow_y - 0.02 * x)).draw(win)
        fletching.setWidth(2)
        fletching.setFill("gray")


if __name__ == "__main__":
    from inspect import cleandoc
    import os

    funcs = []
    for value in list(locals().values()):
        if callable(value) and value.__module__ == __name__:
            if "Helper" not in value.__doc__ and "Example" not in value.__doc__:
                funcs.append(value)

    func_count = len(funcs)

    def print_func_names():
        """Prints the index and name of all of the functions in this script."""
        print("\nFunctions:")
        for i, func in enumerate(funcs, start=1):
            print(f"{i} {func.__name__}")

    print_func_names()

    while True:
        try:
            ans = int(input(f"\nEnter the number of the function to demo (0 to quit) > "))
            if ans == 0:
                print("Goodbye!")
                break
            elif 0 < ans <= func_count:
                os.system("cls" if os.name == "nt" else "clear")
                func = funcs[ans - 1]
                print(f"{'=' * 76}\n{cleandoc(func.__doc__)}\n{'=' * 76}\n")

                res = func()
                if res is not None:
                    print(res)

                print_func_names()
            else:
                raise ValueError("invalid: no such demo exists")
        except ValueError as error:
            print(error)
