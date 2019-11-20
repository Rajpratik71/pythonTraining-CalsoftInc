from math import pow

class Shape:
    def area(self):
        return None

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        print("Area of Square of length {} is {}".format(self.length, pow(self.length,2)))

if __name__ == "__main__":
    length = int(input("Enter length of Square: "))
	square_1 = Square(length)
	print("Area of sqaure of length:%d is %.2f"%(length,square_1.area()))	
	
from math import pow
class Shape:
	def area():
		return 0

class Square(Shape):
	def __init__(self,length):
		self.length = length
	def area(self):
		return pow(self.length ,2)

if __name__=='__main__':
	length = int(input("Enter length of Square: "))
	square_1 = Square(length)
	print("Area of sqaure of length:%d is %.2f"%(length,square_1.area()))