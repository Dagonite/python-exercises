# sock_pairs.py
"""There is a large pile of socks that must be paired by color. Write a function that takes an array of integers 
representing the colour of each sock and return how many pairs of socks with matching colors there are."""


def calculate_sock_pairs(socks):
    unique_socks = set(socks)
    sock_pairs = sum(socks.count(sock) // 2 for sock in unique_socks)
    return sock_pairs


if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 1, 3, 1, 2],
        [10, 10, 10, 10, 10, 20, 30, 20],
        [1, 1, 3, 1, 2, 1, 3, 3, 3, 3],
        [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5],
        [1, 2, 3],
        [1, 1],
    ]

    answers = [
        2,
        3,
        4,
        6,
        0,
        1,
    ]

    for i, test_case in enumerate(test_cases):
        res = calculate_sock_pairs(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)