# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:44:26 2019

@author: pentela.srikrishna
"""

class addd:
    def adding(self,x,y):
        return x+y
def subt(self,x,y):
    return x-y
addd.adding=subt
s=addd()
print(s.adding(3,4))