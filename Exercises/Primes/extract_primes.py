# extract_primes.py
"""Create a function that takes an integer argument and returns a list of prime numbers found in the decimal 
representation of that number (not factors). The list should be in acending order. If a prime number appears more than 
once, every occurance should be listed. If no prime numbers are found, return an empty list."""


def extract_primes(num):
    # set of numbers from 2 to num
    primes = set(range(2, num + 1))
    for i in range(2, int(num ** 0.5 + 1)):
        # remove multiples of current prime from the set
        primes -= set(range(i * 2, num + 1, i))

    # list of representations of num
    num_str = str(num)
    subnums = [
        int(num_str[j : j + i + 1])
        for i in range(len(num_str))
        for j in range(len(num_str) - i)
        if num_str[j] != "0"
    ]

    # check if subnumbers are in primes set
    return sorted([n for n in subnums if n in primes])


print(extract_primes(17))
print(extract_primes(14972))
print(extract_primes(103))
print(extract_primes(80))
print(extract_primes(0))
print(extract_primes(2))
