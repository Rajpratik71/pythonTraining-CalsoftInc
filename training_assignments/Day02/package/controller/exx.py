# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:11:11 2019

@author: pentela.srikrishna
"""

import math
import random 
def get_random():
    return random.random() 
def get_random_from_range(minimum,maximum): 
   return random.randrange(minimum,maximum)
def get_sqrt(number):
    return math.sqrt(number)  
def get_power(number,power):
    return math.pow(number,power) 
def get_factorial(number): 
    return math.factorial(number)
def sin_value(a):
    a = math.pi / 6
    return math.sin(a)
