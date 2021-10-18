"""
Create functions so that function calls like `seven(times(five()))` return the
expected integer.
"""


def identity(x):
    return x


def zero(op=identity):
    return op(0)


def one(op=identity):
    return op(1)


def two(op=identity):
    return op(2)


def three(op=identity):
    return op(3)


def four(op=identity):
    return op(4)


def five(op=identity):
    return op(5)


def six(op=identity):
    return op(6)


def seven(op=identity):
    return op(7)


def eight(op=identity):
    return op(8)


def nine(op=identity):
    return op(9)


def plus(x):
    return lambda y: y + x


def minus(x):
    return lambda y: y - x


def times(x):
    return lambda y: y * x


def divided_by(x):
    return lambda y: y // x


if __name__ == "__main__":
    from random import randint

    base = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    basef = [zero, one, two, three, four, five, six, seven, eight, nine]

    for _ in range(30):
        a, b = randint(0, 9), randint(0, 9)
        operation = f"{base[a]}(plus({base[b]}()))"
        res = basef[a](plus(basef[b]()))
        print("[Pass]" if res == a + b else "[Fail]", f"{operation:<30}={res}")

        a, b = randint(0, 9), randint(0, 9)
        operation = f"{base[a]}(minus({base[b]}()))"
        res = basef[a](minus(basef[b]()))
        print("[Pass]" if res == a - b else "[Fail]", f"{operation:<30}={res}")

        a, b = randint(0, 9), randint(0, 9)
        operation = f"{base[a]}(times({base[b]}()))"
        res = basef[a](times(basef[b]()))
        print("[Pass]" if res == a * b else "[Fail]", f"{operation:<30}={res}")

        a, b = randint(0, 9), randint(1, 9)
        operation = f"{base[a]}(divided_by({base[b]}()))"
        res = basef[a](divided_by(basef[b]()))
        print("[Pass]" if res == a // b else "[Fail]", f"{operation:<30}={res}")
