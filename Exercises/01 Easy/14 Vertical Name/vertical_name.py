# vertical_name.py
"""Create a function that takes a name and prints it out vertically."""

# using a loop
def vertical_name_1(name):
    for ch in name:
        print(ch)


# unpacking name
def vertical_name_2(name):
    print(*name, sep="\n")


# using join method
def vertical_name_3(name):
    print("\n".join(list(name)))


vertical_name_3("Sameul Olo")
