"""
Create a function that takes an integer argument and returns a list of prime
numbers found in the decimal representation of that number (not factors). The
list should be in acending order. If a prime number appears more than once,
every occurance should be listed. If no prime numbers are found, return an empty
list.
"""


def extract_primes(num):
    primes = set(range(2, num + 1))
    for i in range(2, int(num ** 0.5 + 1)):
        primes -= set(range(i * 2, num + 1, i))  # remove multiples of i from the set

    # list of representations of num
    num_str = str(num)
    subnums = [
        int(num_str[j : j + i + 1]) for i in range(len(num_str)) for j in range(len(num_str) - i) if num_str[j] != "0"
    ]

    # return sorted subnumbers which are in primes set
    return sorted([n for n in subnums if n in primes])


def main():
    test_cases = [
        17,
        14972,
        103,
        80,
        0,
        2,
        28521,
    ]

    answers = [
        [7, 17],
        [2, 7, 97, 149],
        [3, 103],
        [],
        [],
        [2],
        [2, 2, 5, 521, 8521],
    ]

    for i, test_case in enumerate(test_cases):
        res = extract_primes(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)


if __name__ == "__main__":
    main()
