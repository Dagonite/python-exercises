# add_names.py
"""Given three arguments: ⁠a dictionary "obj", a key "name", and a "value". Create a function that returns a dictionary 
with that name and value in it as key-value pairs."""


def add_name(obj, name, value):
    obj[name] = value
    return obj


if __name__ == "__main__":
    test_cases = [
        ({}, "Jamie", 2000),
        ({"Caligula": 37}, "Nero", 54),
        ({"Robert the Bruce": 1306, "William Wallace": 1270}, "King Edward", 1239),
    ]

    answers = [
        {"Jamie": 2000},
        {"Caligula": 37, "Nero": 54},
        {"Robert the Bruce": 1306, "William Wallace": 1270, "King Edward": 1239},
    ]

    for i, test_case in enumerate(test_cases):
        res = add_name(test_case[0], test_case[1], test_case[2])
        print("[Pass]" if answers[i] == res else "[Fail]", res)