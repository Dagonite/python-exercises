# multiples_of_three.py
"""Given a range of numbers from 1 to 100, print multiples of 3 in a list."""

from functools import reduce

numbers = range(1, 101)

# imperatively using modulo
threes = []
for n in numbers:
    if n % 3 == 0:
        threes.append(n)
print(threes)

# using unpacking and list slicing to supply start and step args for range()
print([*numbers[2::3]])

# using list comprehension and modulo
print([n for n in numbers if n % 3 == 0])

# using filter and lambda then casting to a list
print(list(filter(lambda n: n % 3 == 0, numbers)))