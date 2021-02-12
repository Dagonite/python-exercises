# odd_numbers_list.py
"""List all odd numbers between 1 and 100."""

list_of_numbers = range(1, 101)

# using list comprehension
print([n for n in list_of_numbers if n % 2])

# using filter and lambda
print(list(filter(lambda n: n % 2, list_of_numbers)))
