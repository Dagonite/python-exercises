"""
Write code which will print a list of numbers 0 to 999 as strings. Strings less
than 3 characters long should have 0s added to the beginning until they reach 3
characters long. The zfill() method can't be used.
"""

print([f"{n:03}" for n in range(1000)])
