'''
1)Write a program to subtract two numbers using magic method(__sub__).

input1: 10 
input2: 5
output: 5

Explanation:
The first input will be the argument of one of the class and the other input will be just a variable.
So when we print(obj of the class - variable) 
should give me the output.
'''

class SubtractMagic:
	def __init__(self,number1):
		self.number1 = number1

	def __sub__(self,number2):
		print("Subtracting {} and {}".format(self.number1,number2))
		return self.number1 - number2
if __name__=='__main__':
	
	subtract_obj = SubtractMagic(10)
	#subtract_obj2 = SubtractMagic(5)
	print(subtract_obj - 5)