# add_names_to_dict.py
"""Given three arguments ⁠— a dictionary "obj", a key "name", and a "value" ⁠— return a dictionary with that name and 
value in it (as key-value pairs)."""


def add_name(obj, name, value):
    obj[name] = value
    return obj


print(add_name({}, "Jamie", 320))
print(add_name({"Caligula": 400}, "Brutus", 300))
print(add_name({"Robert the Bruce": 800, "William Wallace": 500}, "King Edward", 3000))
