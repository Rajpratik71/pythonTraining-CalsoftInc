class FourSidedStructure:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def _get_area(self):
        self.area = self.length * self.breadth


class Rectangle(FourSidedStructure):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)


class Square(FourSidedStructure):
    def __init__(self, side):
        super().__init__(side, side)


p = FourSidedStructure(20, 3)
p._get_area()
print(p.area)
print(p.__dict__)

p = Rectangle(20, 10)
p._get_area()
print(p.area)
print(p.__dict__)

p = Square(20)
p._get_area()
print(p.area)
print(p.__dict__)
