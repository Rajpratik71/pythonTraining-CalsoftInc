"""
 Write a function which will takes a first parameter as *args, newlist as a second parameter. The default value to the newlist  will be "[]".
   Append the args in the list inside the function and print the list.
   call the function as :
   func(1,2,3)
   func(7,8,9, a=[])
   func(8,9,10)
   Explain the observation.
   PS. Don't copy paste from google, try to undestand what's happening in the background and explain in your own words

"""

def kfunc(*args,newlist=[]):
    for arg in args:
        newlist.append(arg)
    print(newlist)

if __name__=='__main__':
    """
    this function will append 1,2,3,4 in newlist 
    """
    kfunc(1,2,3,4)
    """
    this function will append 7,8,9 in newlist=[1,2,3]
    """
    kfunc(7,8,9,newlist=[1,2,3])
    """
    this function will append 8,9,10 in newlist which already has stored values of 1,2,3,4 so output of this func will be [1,2,3,4,8,9,10]
    """
    kfunc(8,9,10)