
import math
from math import pi

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (pi * math.pow(self.radius,2))


if __name__ == "__main__":
    print("Enter the radius of circle: ",end = " ")
    radius = int(input("Enter radius of circle: "))
    circle1 = Circle(radius)
    print("Area of circle is : {}".format(circle1.area()))	