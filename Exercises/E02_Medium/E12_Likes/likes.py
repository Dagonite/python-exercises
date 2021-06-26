"""Write a function that recreates the like system seen on blog posts. The function should take a list of names as 
strings and return a string detailing who liked the post."""


def likes(names):
    n = len(names)
    return [
        "no one likes this",
        "{} likes this",
        "{} and {} like this",
        "{}, {} and {} like this",
        "{}, {} and {others} others like this",
    ][min(4, n)].format(*names, others=n - 2)


if __name__ == "__main__":
    test_cases = [
        [],
        ["Joe"],
        ["Alex", "Sam"],
        ["Adam", "Ben", "Mark"],
        ["Max", "Ali", "Kylee", "Maurice"],
        ["Jaxx", "Zeenat", "Eli", "Grace", "Jordan"],
    ]

    answers = [
        "no one likes this",
        "Joe likes this",
        "Alex and Sam like this",
        "Adam, Ben and Mark like this",
        "Max, Ali and 2 others like this",
        "Jaxx, Zeenat and 3 others like this",
    ]

    for i, test_case in enumerate(test_cases):
        res = likes(test_case)
        print([answers[i] == res], res)