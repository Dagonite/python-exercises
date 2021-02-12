# odd_numbers.py
"""Print all odd numbers between 1 and 100 on separate lines."""

list_of_numbers = list(range(1, 101))

# using modulus
for n in list_of_numbers:
    if n % 2:
        print(n)

# using filter and lambda
for n in filter(lambda n: n % 2, list_of_numbers):
    print(n)

# using a bitwise operator
for n in list_of_numbers:
    if n & 1:
        print(n)

# using the join method
print("".join(str(n) + "\n" for n in list_of_numbers if n % 2))

# using slice notation
for n in list_of_numbers[::2]:
    print(n)

# using a third range argument
for n in range(1, 101, 2):
    print(n)
