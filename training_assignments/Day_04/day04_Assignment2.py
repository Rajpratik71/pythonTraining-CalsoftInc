'''
Program to add two complex numbers(a+ij where 'a'is real number and 'i' is imaginary number) using magic method(__add__).

Example:
input1: 1+2j
input2: 2+1j 
Output: 3+3j

Note:
a -->You will have to take 2 inputs from the user which will be in the same format as the above input1 and input2

b -->the real part(a) and imaginary part(i) will be two attributes of a class and then add both the objects of class to get the expected output
'''
class Complex:
	def __init__(self,real,imaginary):
		self.real = real
		self.imaginary = imaginary 
	
	def __add__(self,other):
		print ("Adding {} and {}".format(self,other))
		return Complex(self.real+other.real, self.imaginary+other.imaginary)

	def __repr__(self):
		return '{}+{}j'.format(self.real,self.imaginary)

if __name__=='__main__':
	
	complex_obj1 = Complex(2,3)
	complex_obj2 = Complex(3,4)
	complex_obj3 = complex_obj1 + complex_obj2
	print("Addition is: ",complex_obj3)