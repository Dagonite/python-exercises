"""q02_house2.py"""

from graphics import GraphWin, Point, Rectangle, Text, Polygon


def main():
    """
    2. Modify the house.py program to give another program house2.py where the
    size of graphics window and the number displayed on the door of the house
    are additional user inputs. Assume that the graphics window is square so
    that the user only has to input a single value for its size. Like the
    original house.py program, the house should fill the entire graphics window.

    Hint: use the setCoords() method.
    """
    door_colour, lights_on, n, size = get_inputs()
    draw_house(door_colour, lights_on, n, size)


def get_inputs():
    door_colour = input("Enter door colour: ")
    lights_bool = input("Are the lights on (y/n): ")
    lights_on = lights_bool[0] == "y"
    n = input("Enter the door number: ")
    size = input("Enter the graphics window size: ")

    return door_colour, lights_on, int(n), int(size)


def draw_house(door_colour, lights_on, n, size):
    win = GraphWin("House", 100 * size, 100 * size)
    win.setCoords(0, 0, 1, 1)

    roof = Polygon(Point(0.01, 0.7), Point(0.22, 0.992), Point(0.78, 0.992), Point(0.992, 0.7))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    draw_rectangle(win, Point(0.008, 0.008), Point(0.992, 0.7), "brown")
    draw_rectangle(win, Point(0.15, 0.008), Point(0.4, 0.45), door_colour)

    # draw door number
    door_n = Text(Point(0.275, 0.35), n)
    door_n.setSize(4 + 2 * size)
    if door_colour == "black":
        door_n.setFill("white")
    door_n.draw(win)

    # draw window
    if lights_on:
        window_colour = "yellow"
    else:
        window_colour = "black"
    draw_rectangle(win, Point(0.55, 0.15), Point(0.85, 0.45), window_colour)


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)


if __name__ == "__main__":
    main()
