'''
8) Write a code to change the functionality of a method of a class during runtime using monkey patching.
Explanation:
Before monkey patching if the method is called it adds the two numbers passed to the method.
After monkey patching if the method is called it subtracts the two numbers passed to the method.
'''

class MonkeyPatchingTest:
	
	def add_functionality(self,input1,input2):
		return input1 + input2
	
def subtract_functionality(self,input1,input2):
	return input1 - input2

MonkeyPatchingTest.add_functionality = subtract_functionality
obj = MonkeyPatchingTest()
output = obj.add_functionality(2,5)
print(output)