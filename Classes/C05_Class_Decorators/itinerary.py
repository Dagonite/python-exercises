# pylint:disable=protected-access

import functools
import inspect

from location import Location
from position import EarthPosition
from utility import auto_repr


def postcondition(predicate):
    def function_decorator(f):
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(f"Post-condition {predicate.__name__} not maintained for {self!r}")
            return result

        return wrapper

    return function_decorator


def invariant(predicate):
    function_decorator = postcondition(predicate)

    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
        return cls

    return class_decorator


def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2


def no_duplicates(itinerary):
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen:
            return False

        already_seen.add(location)

    return True


@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:
    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, name):
        removal_indexes = [index for index, location in enumerate(self._locations) if location.name == name]
        for index in reversed(removal_indexes):
            del self._locations[index]

    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1

        self._locations = self._locations[:stop]


if __name__ == "__main__":
    hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
    stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
    cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
    rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
    maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

    trip = Itinerary.from_locations(rotterdam, cape_town, hong_kong, stockholm)
    trip.remove("Hong Kong")
    print(trip.locations)
