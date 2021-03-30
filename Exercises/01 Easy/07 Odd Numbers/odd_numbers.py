# odd_numbers.py
"""Print all odd numbers between 1 and 100 on separate lines."""

numbers = range(1, 101)

# using modulus
for n in numbers:
    if n % 2:
        print(n)

# using filter and lambda
for n in filter(lambda n: n % 2, numbers):
    print(n)

# using a bitwise operator
for n in numbers:
    if n & 1:
        print(n)

# using the join method
print("\n".join(str(n) for n in numbers if n % 2))

# using slice notation
for n in numbers[::2]:
    print(n)

# using a third range argument
for n in range(1, 101, 2):
    print(n)
