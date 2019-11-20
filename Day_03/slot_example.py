class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


c1 = Car("Honda", "City")

print(c1.__dict__)

print(c1)


class BetterCar:
    __slots__ = "make", "model"

    def __init__(self, make, model):
        self.make = make
        self.model = model


c2 = BetterCar("Honda", "City")

print(c2)

print(c2.__dict__)
