"""Given a range of numbers from 1 to 100, sum all of the odd numbers."""

from functools import reduce

numbers = range(1, 101)

# imperatively using modulo
total = 0
for n in numbers:
    if n % 2:
        total += n
print(total)

# imperatively using a bitwise operator
total = 0
for n in numbers:
    if n & 1:
        total += n
print(total)

# imperatively using list slicing to supply step arg for range
total = 0
for n in numbers[::2]:
    total += n
print(total)

# using sum() and modulo
print(sum(n for n in numbers if n % 2))

# using sum() and a bitwise operator
print(sum(n for n in numbers if n & 1))

# using sum() and list slicing to supply step arg for range
print(sum(numbers[::2]))

# using sum(), filter(), lambda, and modulo
print(sum(filter(lambda n: n % 2, numbers)))

# using sum(), filter(), lambda, and a bitwise operator
print(sum(filter(lambda n: n & 1, numbers)))

# using sum(), filter(), lambda, and list slicing to supply step arg for range
print(sum(filter(lambda n: n, numbers[::2])))

# using an assignment expression and modulo
total = 0
[total := total + n for n in numbers if n % 2]
print(total)

# using an assignment expression and a bitwise operator
total = 0
[total := total + n for n in numbers if n & 1]
print(total)

# using an assignment expression and list slicing to supply step arg for range
total = 0
[total := total + n for n in numbers[::2]]
print(total)

# using reduce(), lambda, and modulo
print(reduce(lambda n, m: n + m if m % 2 else n, numbers))

# using reduce(), lambda, and a bitwise operator
print(reduce(lambda n, m: n + m if m & 1 else n, numbers))

# using reduce(), lambda, and list slicing to supply step arg for range
print(reduce(lambda n, m: n + m, numbers[::2]))

# using a while loop and modulo
total = 0
i = 1
while i < numbers.stop:
    if i % 2:
        total += i
    i += 1
print(total)

# using a while loop and a bitwise operator
total = 0
i = 1
while i < numbers.stop:
    if i & 1:
        total += i
    i += 1
print(total)

# using a while loop and incrementing by step
total = 0
i = 1
step = 2
while i < numbers.stop:
    total += i
    i += step
print(total)

# using the range object's stop value in a formula
print((numbers.stop // 2) ** 2)
