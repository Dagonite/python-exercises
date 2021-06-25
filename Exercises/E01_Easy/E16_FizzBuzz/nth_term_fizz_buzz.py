"""Create a function that takes an integer, n, and returns "Fizz" if it is a multiple of 3, "Buzz" if it is a multiple 
of 5, "FizzBuzz" if it is a multiple of both, or n as a string if neither."""


def fizzbuzz(n):
    return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)


if __name__ == "__main__":
    test_cases = [
        3,
        5,
        6,
        10,
        15,
        17,
        21,
        26,
    ]

    answers = [
        "Fizz",
        "Buzz",
        "Fizz",
        "Buzz",
        "FizzBuzz",
        "17",
        "Fizz",
        "26",
    ]

    for i, test_case in enumerate(test_cases):
        res = fizzbuzz(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)