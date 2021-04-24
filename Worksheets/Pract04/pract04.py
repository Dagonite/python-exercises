# Practical Worksheet 4: Strings and Files

from graphics import GraphWin, Line, Point, Rectangle, Text


def personal_greeting():
    """
    1. Write a personal_greeting() function which, after asking for the user's name, outputs a personalised greeting.
    E.g. for user input "Sam", the function should output the greeting "Hello Sam, nice to see you!". Note: the details
    of the spaces and punctuation).
    """
    first_name = input("Enter your first name: ")
    print("Hello {}, nice to see you!".format(first_name))


def formal_name():
    """
    2. Write a formal_name() function which asks the user to input their given name and family name, and then outputs
    a more formal version of their name. E.g. on input Sam and Brown, the function should output S. Brown (again note
    the spacing and punctuation).
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("{}. {}".format(first_name[0], last_name))


def kilos_to_pounds():
    """
    3. Copy the kilos_to_pounds() conversion function from your pract01.py file. Modify this function so that its output
    takes the form of a message such as "12.34 kilos is equal to 27.15 pounds", where both the user's kilos value and
    the calculated pounds values are displayed to two decimal places.
    """
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print(f"{kilos:.2f} kilos is equal to {pounds:.2f} pounds")


def generate_email():
    """
    4. Suppose the University decides that students’ email addresses should be made up of the first 4 letters of their
    surname, the first letter of their forename, and the final two digits of the year they entered the university,
    separated by dots. Write a function called generate_email() that outputs an email address given a student's details.
    If the user enters: Sam, Brown and 2015. The function should output "brow.s.15@myport.ac.uk".
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    entry_year = input("Enter the year you joined: ")
    email = "{}.{}.{}@myport.ac.uk".format(last_name[:4], first_name[0], entry_year[2:]).lower()
    print(email)


def grade_test():
    """
    5. A teacher awards letter grades for test marks as follows: 8, 9, or 10 marks give an A. 6 or 7 marks give B. 4 or
    5 marks give C. 0, 1, 2, or 3 marks all give F. Using string indexing, write a function, grade_test(), that
    asks the user for a mark (between 0 and 10) and displays the corresponding grade.
    """
    mark = int(input("Enter your mark between 0 and 10: "))
    grade = "FFFFCCBBAAA"
    print("Your grade is", grade[mark])


def graphic_letters():
    """
    6. Write a function, graphic_letters(), that first asks the user to enter a word, opens a graphics window, and then
    allows the user to display the letters of the word at different locations by clicking the mouse once for each letter
    (use the setSize() method of the Text class to make the letters appear big).
    """
    word = input("Enter a word: ")
    win = GraphWin("Letters")
    print("Click anywhere in the graphics window to display each letter of the word")

    for ch in word:
        position = win.getMouse()
        message = Text(position, ch).draw(win)
        message.setSize(20)

    win.getMouse
    win.close()


def sing_a_song():
    """
    7. Write a sing_a_song() function which outputs a “song” based on a single word. The user should be asked for the
    song's word, how many lines long the song should be, and how many times the word should be repeated on each line.
    For example, if the user enters the word "dum" and the numbers 2 and 4, the function should then output the
    following song (note that the spaces are important):

    dum dum
    dum dum
    dum dum
    dum dum
    """
    word = input("Enter the song's word: ")
    lines = int(input("Enter how many lines long the song is: "))
    repeats = int(input("Enter how many times the word is repeated on each line: "))

    row = " ".join([word] * repeats)
    print("\n".join([row] * lines))


def exchange_table():
    """
    8. Write a function, exchange_table(), that gives a table of euros values and their equivalent values in pounds,
    using an exchange rate of 1.108 euros to the pound. The euros values should be 0, 1, 2, ..., 20, and should be right
    justified. The pounds values should be 6 right justified and given to two decimal places (i.e. with decimal points
    lined up and with pence values after the points).
    """
    print("{:>2} {:>3}".format("€", "£"))
    for euros in range(21):
        pounds = euros / 1.108
        print("{:>2} {:>6.2f}".format(euros, pounds))


def make_acronym():
    """
    9. Write a make_acronym() function that allows the user to enter a phrase, and then displays an acronym (the first
    letters of the words in capitals) for that phrase. For example, if the user enters "University of Portsmouth",
    the function should display UOP. Hint: first use the split method to find the words in the inputted string.
    """
    phrase = input("Enter the phrase: ")
    words = phrase.split()
    print("".join(word[0].upper() for word in words))


def name_to_number():
    """
    10. [harder] Write a name_to_number() function that asks the user for their name and converts it into a numerical
    value by adding up the "values" of its letters (where 'a' is 1, 'b' is 2, . . . 'z' is 26). So, for example, "Sam"
    has the value 19 + 1 + 13 = 33.
    """
    first_name = input("Enter your first name: ").lower()
    sequence = " + ".join(str(ord(ch) - 96) for ch in first_name)
    print(sequence, "=", eval(sequence))


def file_in_caps():
    """
    11. Write a file_in_caps() function which displays the contents of a file in capital letters. The name of the input
    file should be entered by the user.
    """
    text_file = input("Enter the text file you want to use (try: 'Battles - Atlas'): ")

    with open(text_file + ".txt", "r") as f:
        file_contents = f.read()

    print("".join(line.upper() for line in file_contents))


def rainfall_chart():
    """
    12. [harder] The file rainfall.txt from the unit web-site contains rainfall data in mm for several UK cities for a
    particular day, in the form:

    Portsmouth 9
    London 5
    Southampton 12

    Write a function, rainfall_chart(), that displays this data as a textual bar chart using one asterisk for each mm of
    rainfall; given the above data the output should be:

    Portsmouth  *********
    London      *****
    Southampton ************
    """
    with open("rainfall.txt", "r") as f:
        file_contents = f.read().split("\n")

    for line in file_contents:
        city, rainfall = line.split()
        print("{:<13} {}".format(city, "*" * int(rainfall)))


def graphical_rainfall_chart():
    """
    13. Now write a graphical version, graphical_rainfall_chart(), that displays a similar bar chart in a graphical
    window but uses filled rectangles instead of sequences of asterisks.
    """
    win = GraphWin("Rainfall Chart", 1050, 300)

    # y axis
    Line(Point(50, 50), Point(50, 260)).draw(win)

    # x axis
    Line(Point(50, 260), Point(1025, 260)).draw(win)

    colours = [
        "red",
        "green",
        "orange",
        "blue",
        "white",
        "yellow",
        "black",
        "brown",
        "gray",
    ]

    with open("rainfall.txt", "r") as f:
        file_contents = f.read().split("\n")

    for i, line in enumerate(file_contents):
        city, rainfall = line.split()

        # label city axis
        Text(Point((i + 1) * 100, 270), city).draw(win)

        # rainfall rectangle
        rectangle = Rectangle(Point((i + 0.5) * 100, 260 - int(rainfall) * 3.7), Point((i + 1.5) * 100, 260))
        rectangle.setFill(colours[i])
        rectangle.draw(win)

    for i in range(6):
        # label rainfall axis
        Text(Point(30, 255 - i * 36), i * 10).draw(win)

    win.getMouse()
    win.close()


def rainfall_in_inches():
    """
    14. [harder] Write a rainfall_in_inches() function that reads the rainfall data from rainfall.txt, and outputs the
    data to a file named rainfall_inches.txt where all the mm values are converted to inches (there are 25.4mm in an
    inch). The inch values should be given to two decimal places, so the Portsmouth line will become:

    Portsmouth 0.35
    """
    with open("rainfall.txt", "r") as f:
        file_contents = f.read().split("\n")

    with open("rainfall_inches.txt", "w") as out_file:
        for line in file_contents:
            city, rainfall = line.split()
            print("{:<13} {:.2f}".format(city, int(rainfall) / 25.4), file=out_file)


def wc():
    """
    15. [harder] In Linux, there is a command called wc which reports the number of characters, words and lines in a
    file. Write a function wc() which performs the same task. The name of the file should be entered by the user.
    """
    text_file = input("Enter the text file you want to use (try: 'quotation'): ") + ".txt"

    with open(text_file, "r") as f:
        file_contents = f.read()

    characters = file_contents.count("")
    print("There are", characters, "characters in", text_file)

    words = len(file_contents.split())
    print("There are", words, "words in", text_file)

    lines = sum(1 for line in file_contents.split("\n"))
    print("There are", lines, "lines in", text_file)


if __name__ == "__main__":
    funcs = [
        personal_greeting,
        formal_name,
        kilos_to_pounds,
        generate_email,
        grade_test,
        graphic_letters,
        sing_a_song,
        exchange_table,
        make_acronym,
        name_to_number,
        file_in_caps,
        rainfall_chart,
        graphical_rainfall_chart,
        rainfall_in_inches,
        wc,
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
