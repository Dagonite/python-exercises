"""Write a function that takes a signature which is a list of integers and the first n elements. The signature is the 
start of the tribonacci sequence. A number in the tribonacci sequence is the sum of the 3 previous values. Signature 
will always contain 3 numbers; n will always be a non-negative integer; if n == 0, then return an empty list."""


def tribonacci(signature, n):
    res = signature
    for _ in range(n):
        res.append(sum(res[-3:]))
    return res[:n]


if __name__ == "__main__":
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
    assert tribonacci([1, 1, 1], 1) == [1]
    assert tribonacci([300, 200, 100], 0) == []