# sum_odd_numbers.py
"""Given a range of numbers from 1 to 100, sum all of the odd numbers in the range."""

from functools import reduce

numbers = range(1, 101)

# imperatively using modulo
total = 0
for n in numbers:
    if n % 2:
        total += n
print(total)

# using sum and modulo
print(sum(n for n in numbers if n % 2))

# using sum and list slicing
print(sum(n for n in numbers[::2]))

# using sum and the third range arg
print(sum(n for n in range(1, 100, 2)))

# using sum, filter, lambda, and modulo
print(sum(filter(lambda n: n % 2, numbers)))

# using augmented assignment and modulo
total = 0
[total := total + n for n in numbers if n % 2]
print(total)

# using reduce, lambda, and modulo
print(reduce(lambda n, m: n + m if m % 2 else n, numbers))
