"""
1) Write a function which will takes a first parameter as *args, newlist as a second parameter. The default value to the newlist  will be "[]".
   Append the args in the list inside the function and print the list.
   call the function as :
   func(1,2,3)
   func(7,8,9, a=[])
   func(8,9,10)
   Explain the observation.
   PS. Don't copy paste from google, try to undestand what's happening in the background and explain in your own words
"""


def kwargdemo(*args, newlist=[]):
	for arg in args:
		newlist.append(arg)
	print(newlist)

if __name__=='__main__':
    """
        This call will  append arguments 1,2,3 to empty newlist
    """
    kwargdemo(1, 2, 3)

    """
        This call will  append arguments 8,9,10 to empty newlist
    """
    kwargdemo(8, 9, 10)

    """
            This call will  append arguments 1,2,3 to  newlist with items
    """
    kwargdemo(7, 8, 9, newlist=[1, 2])






