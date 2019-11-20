import math
class Circle:
    def area_of_circle(radius):
        return (math.pi*(math.pow(radius,2)))
if __name__ == '__main__':    
    radius = int(input('Enter the radius of circle'))
    print('area of circle is {}'.format(Circle.area_of_circle(radius)))