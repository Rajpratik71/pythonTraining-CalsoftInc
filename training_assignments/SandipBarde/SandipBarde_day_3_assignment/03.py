class Shape:
    def __init__(self):
        pass
    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def Area(self):
        return (self.length*self.length)
a = Square(4)
print(a.Area())
