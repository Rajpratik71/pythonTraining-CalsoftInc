# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:22:07 2019

@author: pentela.srikrishna
"""

class shape:
    def area():
        return 0
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
if __name__=='__main__':
    ln=int(input('enter length'))
    square1=square(ln)
    print((ln,square1.area()))
    
        