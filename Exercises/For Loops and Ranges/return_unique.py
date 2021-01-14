# return_unique.py
"""In each input list, every number repeats at least once, except for two. Write a function that returns the two unique 
numbers."""


def return_unique(lst):
    return [n for n in lst if lst.count(n) == 1]


print(return_unique([1, 2, 3, 4, 5, 1, 2, 3]))
print(return_unique([1, 1, 1, 2, 2, 2, 3, 4]))
print(return_unique([1, 2, 2, 3, 4, 4, 5, 5]))
