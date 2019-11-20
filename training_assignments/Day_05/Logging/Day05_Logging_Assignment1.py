'''
1. Write a python program and add some log statemnts with different levels and check for default log level and also change the default log level to some other level and check again.
'''


import logging
logging.basicConfig(level=logging.DEBUG)
class Complex:
	def __init__(self,real,imaginary):
		self.real = real
		self.imaginary = imaginary 
	
	def __add__(self,other):
		logging.debug("Entry:__add__")
		logging.info("Adding {} and {}".format(self,other))
		return Complex(self.real+other.real, self.imaginary+other.imaginary)

	def __repr__(self):
		return '{}+{}j'.format(self.real,self.imaginary)

if __name__=='__main__':
	
	complex_obj1 = Complex(2,3)
	complex_obj2 = Complex(3,4)
	complex_obj3 = complex_obj1 + complex_obj2
	logging.warning("Addition is: %s",complex_obj3)