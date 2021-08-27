"""
When using kwargs for a class constructor; the created attributes are public and 
immutable. Because we don't know the attribute names in advance we can't use the 
property decorator. Can work around this by using the dunder getattr and dunder 
setattr methods.
"""

import traceback


class Vector:
    """An n-dimensional vector."""

    def __init__(self, **compenents) -> None:
        private_components = {f"_{k}": v for k, v in compenents.items()}
        self.__dict__.update(private_components)

    def __getattr__(self, name):
        private_name = f"_{name}"
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError(f"{self!r} object has no attribute {name!r}")

    def __setattr__(self, name, value) -> None:
        raise AttributeError(f"Can't set attribute {name!r}")

    def __delattr__(self, name):
        raise AttributeError(f"Can't delete attribute {name!r}")

    def __repr__(self):
        return f"{type(self).__name__}" + "({})".format(", ".join(f"{k[1:]}={v}" for k, v in self.__dict__.items()))

    def _args(self):
        return {k[1:]: v for k, v in self.__dict__.items()}


class ColoredVector(Vector):

    COLOR_INDEXES = ("red", "green", "blue")

    def __init__(self, red, green, blue, **compenents):
        super().__init__(**compenents)
        self.__dict__["_color"] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__["_color"][channel]

    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__["_color"][channel] = value

    def _args(self):
        args = {
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
        }
        args.update(super()._args())
        del args["color"]
        return args


v = Vector(p=5, q=2)
print(v.p)

# show that there is a key error when accessing an undefined attribute
try:
    print(v.x)
except Exception as exc:
    traceback.print_exc()
    print()

# show that current attributes are immutable
try:
    v.y = 3
except Exception as exc:
    traceback.print_exc()
    print()

# show that current attributes can't be deleted
try:
    del v.p
except Exception as exc:
    traceback.print_exc()
    print()

cv = ColoredVector(red=28, green=113, blue=53, p=4, q=13)
print(cv)
