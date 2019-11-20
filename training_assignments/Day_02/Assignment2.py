def kwargdemo(*args, newlist=[]):
	for arg in args:
		newlist.append(arg)
	print(newlist)

if __name__=='__main__':
	kwargdemo(1,2,3)
	'''
	The above call will just append arguments 1,2,3 to empty newlist
	'''
	#kwargdemo(7,8,9,a=[])
	'''
	The above call gives TypeError: kwargdemo() got an unexpected keyword argument 'a' since we do not have any argument with name so match is not found. This is because we have declared newlist as keyword argument.
	'''
	kwargdemo(8,9,10)
	'''
	Since we did not passed newlist i.e. keyword argument in this call, it took it's default newlist reference since state is maintained.
	'''


