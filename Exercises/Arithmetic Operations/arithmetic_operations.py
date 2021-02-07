# arithmetic_operations.py
"""Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and 
division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21")."""

from operator import add, sub, floordiv, mul


def arithmetic_operation(equation):
    OPS = {"+": add, "-": sub, "*": mul, "//": floordiv}
    a, op, b = equation.split()

    try:
        return OPS[op](int(a), int(b))
    except ZeroDivisionError:
        return -1


print(arithmetic_operation("11 + 10"))
print(arithmetic_operation("8 - 4"))
print(arithmetic_operation("6 * 7"))
print(arithmetic_operation("24 // 8"))
print(arithmetic_operation("5 // 0"))
