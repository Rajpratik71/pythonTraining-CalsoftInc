class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.14
    def area(self):
        return (self.PI* self.radius * self.radius)

if __name__ == "__main__":
    r = int(input("Enter the radius of circle\n"))
    c = Circle(r)
    print( c.area())
