# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:44:55 2019

@author: pentela.srikrishna
"""

def decorator(func):
    def wrapper():
        print("I am the decorator")
        func()
        return wrapper 
    

@decorator
def function():
    print("I am the function")
obj=decorator.wrapper()
print(obj)
