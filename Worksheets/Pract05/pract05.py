"""Practical Worksheet 5: Using functions"""

import math

from graphics import Circle, GraphWin, Line, Point, Text


def circumference_of_circle(radius=None):
    """
    1. The pract05.py file contains a function area_of_circle() which has a
    parameter representing a circle's radius, and returns the area of the
    circle. Write a similar function called circumference_of_circle() that has a
    radius parameter and returns the circumference of the circle.
    """
    if radius is None:
        radius = float(input("Enter the radius > "))
    return 2 * math.pi * radius


def area_of_circle(radius):
    """Helper function that returns the area of a circle."""
    return math.pi * radius ** 2


def circle_info():
    """
    2. Write a function circle_info() which asks the user to input the radius of
    a circle, and then outputs a message that includes both the area and the
    circumference of the circle (displayed to three decimal places). If the user
    enters a radius of 5, then the output message might be 'The area is 78.540
    and the circumference is 31.416'. Your function should call both previous
    functions to do the calculations.
    """
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print(f"The area is {area:.3f} and the circumference is {circumference:.3f}")


def draw_circle(win, centre, radius, colour):
    """Helper function for drawing a circle."""
    circle = Circle(centre, radius).draw(win)
    circle.setFill(colour)
    circle.setWidth(2)


def draw_brown_eye_in_centre():
    """
    3. The draw_circle() function in pract05.py draws a circle on a graphics
    window with a given centre point, radius and colour. Complete the supplied
    draw_brown_eye_in_centre() function so that it calls draw_circle() three
    times in order to draw a brown 'eye' in the centre of a graphics window. The
    radii of the white, brown, and black circles should be 60, 30, and 15
    respectively.
    """
    win = GraphWin()
    centre = Point(100, 100)
    radius = 60
    colours = ["white", "brown", "black"]

    for colour, divisor in zip(colours, [1, 2, 4]):
        draw_circle(win, centre, radius / divisor, colour)

    win.getMouse()
    win.close()


def draw_letter_E():
    """
    4. Write a function draw_block_of_stars() which has two parameters width and
    height, and outputs a rectangle of asterisks of the appropriate dimensions.
    For example, the function call 'draw_block_of_stars(5, 3)' should result in
    the following output:

    *****
    *****
    *****

    Now, write a function draw_letter_E() that displays a large capital letter
    E; for example:

    **********
    **********
    **
    **
    ********
    ********
    **
    **
    **********
    **********

    Your function should work by calling the draw_block_of_stars() function an
    appropriate number of times.
    """
    draw_block_of_stars(10, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(8, 2)
    draw_block_of_stars(2, 2)
    draw_block_of_stars(10, 2)


def draw_block_of_stars(width, height):
    """Helper function for printing a block of stars."""
    for _ in range(height):
        print("*" * width)


def draw_pair_of_brown_eyes():
    """
    5. Add code to the supplied draw_brown_eye() function so that, by calling
    draw_circle() three times, it draws a single brown eye, where the graphics
    window, centre point and radius of the eye are all given as parameters to
    your function. Now, by using your completed draw_brown_eye() function, write
    a draw_pair_of_brown_eyes() function (without parameters) that draws a pair
    of eyes on a graphics window.
    """
    win = GraphWin("Brown eyes", 300, 200)
    draw_brown_eye(win, Point(90, 100), 60)
    draw_brown_eye(win, Point(210, 100), 60)

    win.getMouse()
    win.close()


def draw_brown_eye(win, centre, radius):
    """Helper function for drawing a brown eye."""
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius / 2, "brown")
    draw_circle(win, centre, radius / 4, "black")


def distance_between_points(p1=None, p2=None):
    """
    6. Write a function distance_between_points() that has two parameters, p1
    and p2, each of type Point, and returns the distance between them. This
    function should use the formula for Pythagoras' Theorem, as in Pract02. The
    function call 'distance_between_points(Point(1, 2), Point(4, 6))' should
    result in the value 5.0 being returned.

    Hint: you'll need to use the getX and getY methods to get the x and y
    coordinates of points p1 and p2.
    """
    if p1 is None or p2 is None:
        x1 = float(input("Enter x of p1 > "))
        y1 = float(input("Enter y of p1 > "))
        p1 = Point(x1, y1)

        x2 = float(input("Enter x of p2 > "))
        y2 = float(input("Enter y of p2 > "))
        p2 = Point(x2, y2)

    p1X = p1.getX()
    p1Y = p1.getY()

    p2X = p2.getX()
    p2Y = p2.getY()

    return math.sqrt((p2X - p1X) ** 2 + (p2Y - p1Y) ** 2)


def draw_letter_A():
    """
    7. It should be clear that it is impossible to output letters such as 'A' or
    'O' using only the draw_block_of_stars() function. To allow for more complex
    letters such as these, write a new function draw_blocks() that outputs up to
    four rectangles next to each other (consisting of spaces, then asterisks,
    then spaces and finally asterisks, all of the same height). The widths of
    the four rectangles and their common height should be parameters. The call
    draw_blocks(0, 5, 4, 3, 2) will result in the output:

    *****    ***
    *****    ***

    (with no space before the first asterisks due to the 0 argument). Now, write
    a function draw_letter_A that uses draw_blocks() in order to display a large
    capital A in asterisks, such as:

     ********
     ********
    **      **
    **      **
    **********
    **********
    **      **
    **      **
    **      **
    """
    draw_blocks(1, 8, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 2)
    draw_blocks(0, 10, 0, 0, 2)
    draw_blocks(0, 2, 6, 2, 3)


def draw_blocks(space1, width1, space2, width2, height):
    """Helper function for printing asterisk blocks."""
    for _ in range(height):
        print(" " * space1, end="")
        print("*" * width1, end="")
        print(" " * space2, end="")
        print("*" * width2)


def draw_letter_B():
    """
    Example function for drawing the lettter B.

    ********
    **      **
    **       **
    **      **
    ********
    **      **
    **       **
    **       **
    **********
    """
    draw_blocks(0, 9, 0, 0, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 8, 0, 0, 1)
    draw_blocks(0, 2, 6, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 2, 7, 2, 1)
    draw_blocks(0, 10, 0, 0, 1)


def draw_letter_C():
    """
    Example function for drawing the lettter B.

       ******
     **********
    **        **
    **
    **
    **
    **        **
     **********
       ******
    """
    draw_blocks(3, 6, 0, 0, 1)
    draw_blocks(1, 10, 0, 0, 1)
    draw_blocks(0, 2, 8, 2, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 0, 0, 1)
    draw_blocks(0, 2, 8, 2, 1)
    draw_blocks(1, 10, 0, 0, 1)
    draw_blocks(3, 6, 0, 0, 1)


def draw_four_pairs_of_brown_eyes():
    """
    8. Write a draw_four_pairs_of_brown_eyes() function (which doesn't have
    parameters) that opens a graphics window and allows the user to draw four
    pairs of eyes. Each pair is drawn by clicking the mouse twice: the first
    click gives the centre of the left-most eye, and the second gives any point
    on the outer circumference of this eye.

    Hint: this function should call the distance_between_points() function from
    exercise 6 to obtain the radius of each eye, as well as the draw_brown_eye()
    function from exercise 5 to draw the eyes.
    """
    win = GraphWin("Four pairs of brown eyes", 1200, 800)
    for _ in range(4):
        p1 = win.getMouse()
        p2 = win.getMouse()
        radius = distance_between_points(p1, p2)
        draw_brown_eye(win, p1, radius)
        draw_brown_eye(win, (Point(p1.getX() + radius * 2, p1.getY())), radius)

    win.getMouse()
    win.close()


def construct_vision_chart():
    """
    9. [harder] Write a display_text_with_spaces() function which will display a
    given string at a given point-size at a given position on a given graphics
    window (i.e. it should have four parameters). The string should be displayed
    with spaces between each character (for example, hello would be displayed
    as h e l l o). Now, using this function, write another function,
    construct_vision_chart(), that constructs an optician's vision chart. Your
    function should first open a graphics window. It should then ask the user
    for six strings, displaying them on the graphics window as they are entered.
    The strings should be displayed in upper case, and from the top of the
    window to the bottom with descending point sizes of 30, 25, 20, 15, 10, and
    5 (make sure that the lines are well-spaced out — you might need to
    experiment a little with spacing).
    """
    win = GraphWin("Vision chart", 500, 400)

    for i in range(6):
        line = input("Give me a string: ")
        size = 30 - 5 * i
        y = 60 * (i + 1)
        display_text_with_spaces(win, line, size, y)

    win.getMouse()
    win.close()


def display_text_with_spaces(win, line, size, y):
    """Helper function for displaying spaced text on a graphics window."""
    upper_line = line.upper()
    spaced_line = upper_line.replace("", " ")[1:-1]
    message = Text(Point(250, y), spaced_line).draw(win)
    message.setFace("courier")
    message.setSize(size)


def draw_stick_figure_family():
    """
    10. [harder] Write a draw_stick_figure_family() function. This function
    should display a group of four or five stick figures (representing a family)
    in a graphics window. All the stick figures should be the same shape (e.g.
    that of exercise 1, pract03), but they should be of different sizes and
    positions. Begin by copying your draw_stick_figure() function from
    'pract03.py', and changing it so that it has three parameters, representing
    a graphics window, the position of the figure (a Point) and its size (an
    int). What the position and size mean exactly is up to you. Your
    draw_stick_figure_family() function should contain just four or five calls
    to the modified version of draw_stick_figure().
    """
    win = GraphWin("Stick Figure Family", 250, 200)
    draw_stick_figure(win, Point(50, 50), 25)
    draw_stick_figure(win, Point(100, 50), 20)
    draw_stick_figure(win, Point(150, 50), 18)
    draw_stick_figure(win, Point(200, 50), 15)
    win.getMouse()
    win.close()


def draw_stick_figure(win, position, size):
    """Helper function for drawing a stick figure."""
    posX = position.getX()
    posY = position.getY()

    Circle(position, size).draw(win)
    Line(Point(posX, posY + size), Point(posX, posY + size * 3)).draw(win)
    Line(Point(posX - size, posY + size * 2), Point(posX + size, posY + size * 2)).draw(win)
    Line(Point(posX, posY + size * 3), Point(posX - size, posY + size * 5)).draw(win)
    Line(Point(posX, posY + size * 3), Point(posX + size, posY + size * 5)).draw(win)


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
