'''
6)Write a  decorator which checks if the input value is an integer and is greater than 0 and should return an error message if the condition fails.
The decorator is used above a function which adds two numbers.

Example1:
input: 2,3
output:5
Example2:
input: a,3
output:"Incorrect parameter passed.Please give an integer value"
Example3:
input: 0,3

output:"Incorrect parameter passed.Please give an integer greater than zero"

Explanation:
After the user has provided the input, firstly the decorator verifies that the input value are integers and greater than zero,
once verified then the values are passed onto the add function(over which the decorator is used) where the values are added.
'''

def int_validator(func):
	def wrapper(input1,input2):
		if not(isinstance(input1,int)) or not(isinstance(input2,int)):
			print("Incorrect parameter passed.Please give an integer value")
		else:
			if input1 <= 0 or input2 <= 0:
                        	print("Incorrect parameter passed.Please give an integer greater than zero")
			else:
				return	func(input1,input2)
	return wrapper

@int_validator
def add(input1,input2):
	return input1+input2


print(add(2,3))
#print(add(0,5))
#print(add('a',5))