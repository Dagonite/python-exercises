# sum_odd_numbers.py
"""Sum all odd numbers between 1 and 100."""

from functools import reduce

list_of_numbers = list(range(1, 101))

# imperative way
total = 0
for n in list_of_numbers:
    if n % 2:
        total += n
print(total)

# using := to assign to variables within an expression
total = 0
[total := total + n for n in list_of_numbers if n % 2]
print(total)

# using reduce and lambda
print(reduce(lambda n, m: n + m if m % 2 else n, list_of_numbers))

# using sum, filter, and lambda
print(sum(filter(lambda n: n % 2, list_of_numbers)))