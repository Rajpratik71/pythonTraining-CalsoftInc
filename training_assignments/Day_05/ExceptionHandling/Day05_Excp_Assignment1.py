'''
1. Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

def division(dividend,divisor):
	return dividend / divisor

try:
	quotient = division(5,0)
except:
	print("Divisor can not be 0")