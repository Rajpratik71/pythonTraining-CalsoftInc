'''
7)Identify the missing piece of code in below program and write the correct answer to remove the error which we get when print statements are called
'''

def decorator(func):
	def wrapper():
		print("I am the decorator")
		func()
	return wrapper
@decorator
def function():
	print("I am the function")
function()
'''
Explanation:
When we execute the above code, we get the error "TypeError: 'NoneType' object is not callable" but the expected output is
I am the decorator
I am the function.

Hint:
Decorators are expected to return "something".
'''
