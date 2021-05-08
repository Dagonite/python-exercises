# Practical Worksheet 9: Using Lists

from graphics import GraphWin, Polygon


def display_date(day, month, year):
    """
    1. Using a list, write a function display_date() that takes three integer parameters representing a day, month and
    year, and outputs the date as a (readable) string. For example, the call display_date(14, 2, 2011) should display:

    14 Feb 2011

    Hint: put strings representing all the months into a list, and index this list."""
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month = months[month - 1][:3]
    print(day, month, year)


def word_lengths(words):
    """
    2. Write a function word_lengths() that takes a list of strings as a parameter, and displays each of the words
    alongside its length. E.g, the call word_lengths(["bacon", "jam", "spam"]) should result in the following output:

    bacon 5
    jam 3
    spam 4
    """
    for word in words:
        print(word, len(word))


def draw_hexagon():
    """
    3. Write a function draw_hexagon() that allows the user to draw a hexagon (a shape with six vertices (points)) on a
    graphics window. The function should allow the user to click on their chosen locations for the hexagon's vertices,
    and then draw the hexagon (filled in red). Hint: A hexagon is a Polygon, and you can make a Polygon object from a
    list of Point objects.
    """
    win = GraphWin("Hexagon", 500, 500)
    vertexes = []
    for vertices in range(6):
        vertexes.append(win.getMouse())
        print("That's point", vertices + 1)
    hexagon = Polygon(vertexes[0], vertexes[1], vertexes[2], vertexes[3], vertexes[4], vertexes[5]).draw(win)
    hexagon.setFill("red")

    win.getMouse()
    win.close()


def test_marks():
    """
    4. A test at a university is marked out of 5. Write a function test_marks() that allows a lecturer to input the unit
    marks of all her students, providing a suitable way for her to say she’s finished entering marks. The function
    should then output the number of students who have achieved each possible mark. For example, if the lecturer enters
    the marks 4, 0, 4, 1, 1, 4, 3 and 5, the function should output:

    1 student(s) got 0 marks
    2 student(s) got 1 marks
    0 student(s) got 2 marks
    1 student(s) got 3 marks
    3 student(s) got 4 marks
    1 student(s) got 5 marks
    """
    marks = []
    while True:
        mark = input("\nEnter a mark ('q' to quit): ").strip()
        if mark == "" or mark[0] == "q":
            break
        elif mark.isdigit():
            mark = int(mark)
            if mark > 5:
                print("Error: Input out of range")
                continue
            marks.append(mark)
        else:
            print("Error: Invalid input")

    if marks:
        for i in range(6):
            n = marks.count(i)
            print(n, "student(s) got", i, "mark(s)")


def draw_bar_chart(numbers):
    """
    5. Write a function draw_bar_chart() that takes a list of integers as a parameter, and draws a simple downwards-
    facing bar chart of # symbols for the data in the list. For example, the call draw_bar_chart([3, 1, 2]) should
    result in the following output:

    # # #
    #   #
    #
    """
    for row_count in range(max(numbers)):
        print(" ".join(["#" if item > row_count else " " for item in numbers]))


if __name__ == "__main__":
    funcs = [
        display_date,
        word_lengths,
        draw_hexagon,
        test_marks,
        draw_bar_chart,
    ]

    no_of_funcs = len(funcs)
    print("".join(func.__doc__ for func in funcs))

    while True:
        try:
            print("\nFunctions which have parameters will take arbitrary args")
            func_number = int(input("Enter the number of the function to demo (0 to quit): "))

            if func_number == 0:
                print("Goodbye!")
                break
            elif func_number == 1:
                print()
                funcs[func_number - 1](15, 5, 2017)
            elif func_number == 2:
                print()
                funcs[func_number - 1](["bacon", "jam", "spam"])
            elif func_number == 5:
                print()
                funcs[func_number - 1]([4, 5, 1, 2, 3, 8])
            elif 0 < func_number <= no_of_funcs:
                print()
                funcs[func_number - 1]()
            else:
                raise ValueError
        except Exception:
            print("Invalid input")