'''
3. Complete the below program to run successfully:
	a. Write user defined exception class for User_defined_exception1, User_defined_exception2
	b. Handle the user defined exception writing #appropriate message to user

# we need to guess this alphabet till we get it right
'''

alphabet = 'k'
class  SmallerAlphabetException(Exception):
	def __init__(self,msg):
		self.msg = msg

class GreaterAlphabetException(Exception):
	def __init__(self,msg):
		self.msg = msg

while True:
	try:
		foo = input( "Enter an alphabet: ")

		if foo < alphabet:
			raise SmallerAlphabetException("Entered alphabet {} is smaller than alphabet {}".format(foo,alphabet))
		elif foo > alphabet:
			raise GreaterAlphabetException("Entered alphabet {} is greater than alphabet {}".format(foo,alphabet))
	
	except SmallerAlphabetException as sae:
		print(sae)
	except GreaterAlphabetException as gae:
		print(gae)
	else: 
		print("Congratulations! You guessed it correctly.")
