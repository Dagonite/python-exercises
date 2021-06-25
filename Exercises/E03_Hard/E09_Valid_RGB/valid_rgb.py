"""Given an RGB(A) CSS color, determine whether its format is valid or not. Create a function that takes a string (e.g. 
"rgb(0, 0, 0)") and returns True if the format is correct, otherwise False."""


def valid_color(color):
    def rgb(r, g, b):
        return all(0 <= p <= 255 for p in (r, g, b))

    # pylint: disable=unused-variable
    def rgba(r, g, b, a):
        return rgb(r, g, b) and 0 <= a <= 1

    try:
        nospace = "rgb(" in color or "rgba(" in color
        return nospace and eval(color.replace("%", "*2.55"))
    except (SyntaxError, TypeError):
        return False