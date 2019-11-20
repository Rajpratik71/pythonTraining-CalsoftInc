# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:45:38 2019

@author: pentela.srikrishna
"""

@decorator
def hello_decorator(func):
    def check():
        a=int(input('enter the number'))
        b=int(input('enter the number'))
        if a>0 and b>0:
            c=a.__add__(b)
            print(c)
        else:
            print("Incorrect parameter passed.Please give an integer value")
check=hello_decorator(check())
check()
    
