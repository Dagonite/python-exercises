class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return format(self)

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return f"{latitude}° {self.latitude_hemisphere}, {longitude}° {self.longitude_hemisphere}"


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__


if __name__ == "__main__":
    mauna_kea = EarthPosition(19.82, -155.47)
    print(mauna_kea)

    olympus_mons = MarsPosition(18.65, -133.8)
    print(repr(olympus_mons))

    k2 = EarthPosition(35.88, 76.51)
    print(f"{k2:.0}")
