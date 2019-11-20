import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        ar = math.pi*self.radius*self.radius
        return ar

if __name__=='__main__':
    c = Circle(10)
    area = c.Area()
    print(f'area of the circle is {area}')
