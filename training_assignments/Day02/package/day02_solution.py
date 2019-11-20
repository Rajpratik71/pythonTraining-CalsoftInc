# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:19:53 2019

@author: pentela.srikrishna
"""
# Function definition with arguments
def  mounting(*args, newlist=[]):
     # This is a docstring of a function
    """
    This is function level docstring
    Args:
        args:
        newlist[]:
    Returns:
     """
    for i in args:
	    newlist.append(i)#values are add to empty list
    print(newlist)
# Entry point for the execution of the script
if __name__=='__main__':# Checking the the script name is __main__
   mounting(1,2,3) # function call
   
   
   
# Function definition with arguments
def get_quadratic_solution(a,b,c):
    # This is a docstring of a function
    """
    This is function level docstring
    it is maths statements
     """
    x1 =-b/(2*a)
    x2 =(abs(b*b - 4*a*c)) / (2*a)
    print(x1)
    print(x2)
# Entry point for the execution of the script
if __name__=='__main__':
    get_quadratic_solution(1,2,3)# function call