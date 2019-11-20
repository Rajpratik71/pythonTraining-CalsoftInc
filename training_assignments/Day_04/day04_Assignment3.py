'''
3)Identify the missing piece of code in below program and write the correct answer to remove the error which we get when print statements are called
'''

class Checking:
	def __init__(self, name):
		self.name = name
	
	def __getattr__(self,nonexisting_item):
		return nonexisting_item

obj = Checking("Calsoft")
print(obj.checking_the_object)

obj.creating_the_object = "Calsoft.Inc"

print(obj.creating_the_object)

