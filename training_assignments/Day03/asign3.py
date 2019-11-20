# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:50:26 2019

@author: venkata.ramaiah
"""
############### Question No(1)   ###############
import math
class Circle:
    def __init__(self, radius):
       self.radius = radius
    def Area(self):
        argument = math.pi*self.radius*self.radius
        return argument
 
if __name__=='__main__':
   c = Circle(10)
   area = c.Area()
   print(f'area of the circle is {area}')    
    
 #######################  end ########################   
    

