"""
Given an RGB(A) CSS color, determine whether its format is valid or not. Create
a function that takes a string (e.g. rgb(0, 0, 0)) and returns True if the
format is correct, otherwise False.

RGB values must be values between 0 and 255 (inclusive) or a percentage between
0 and 100 (inclusive).

Alpha values must be between 0 and 1 (inclusive).
"""


def valid_color(color):
    def _rgb(r, g, b):
        return all(0 <= p <= 255 for p in (r, g, b))

    # pylint: disable=unused-variable
    def _rgba(r, g, b, a):
        return _rgb(r, g, b) and 0 <= a <= 1

    try:
        nospace = "rgb(" in color or "rgba(" in color
        return nospace and eval("_" + color.replace("%", "*2.55"))
    except (SyntaxError, TypeError):
        return False


if __name__ == "__main__":
    test_cases = [
        "rgb(100, 200, 50)",
        "rgb(20, 30, 60)",
        "rgb(255, 100, 5)",
        "rgb(100%, 200, 300)",
        "rgb(10,15,10)",
        "rgba(10, 40, 20, 0.5)",
        "rgba(90%, 20%, 0, 50%)",
        "rgba(120%, 200, 10, 1)",
        "rgb 15, 15, 15",
        "(30, 20, 10, 0.1)rgba",
    ]

    answers = [
        True,
        True,
        True,
        False,
        True,
        True,
        False,
        False,
        False,
        False,
    ]

    for i, test_case in enumerate(test_cases):
        res = valid_color(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
