# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:42:04 2019

@author: vamsi.reddy
"""
class Shape:
    def Area(length):
        return(0)
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def Area(self):
        return(pow(self.length,2))
if __name__ == '__main__':
    obj = Square(30)
    print(obj.Area())