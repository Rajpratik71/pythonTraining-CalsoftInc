'''
2. Write a user defined exception class "NegativePriceException" and use it to raise as exception when a price of an item entered by user is negative.
'''
class NegativePriceException(Exception):
	def __init__(self,msg):
		self.msg = msg
def check_negative(price):
	if price < 0:
		raise NegativePriceException("Price can not be negative")
if __name__=='__main__':
	price = int(input("Enter integer number"))
	try:
		check_negative(price)
	except NegativePriceException as npe:
		print(npe)
		
		