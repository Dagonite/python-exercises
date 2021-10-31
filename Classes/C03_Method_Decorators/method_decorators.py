# pylint:disable=attribute-defined-outside-init

import iso6346


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(owner_code=owner_code, serial=ShippingContainer._generate_serial())
        self.__dict__.update(kwargs)

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @property
    def celsius(self):
        return round(float(self._celsius), 1)

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return round(float(RefrigeratedShippingContainer._c_to_f(self.celsius)), 1)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category="R")


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)


if __name__ == "__main__":
    r = RefrigeratedShippingContainer.create_empty("MAE", 36, celsius=-21)
    r.celsius = -24.4
    print(f"{r.celsius = }")
    print(f"{r.fahrenheit = }")
    print(f"{r.bic = }")
    print(f"{r.volume_ft3 = }")

    s = ShippingContainer("COS", 40, ["pharmaceuticals"])
    print(f"\n{s.contents = }")
    print(f"{s.bic = }")
    print(f"{s.volume_ft3 = }")

    h = HeatedRefrigeratedShippingContainer("EIM", 36, ["aerosols"], celsius=-4)
    print(f"\n{h.celsius = }")
    print(f"{h.fahrenheit = }")
    print(f"{h.bic = }")
    print(f"{h.volume_ft3 = }")
