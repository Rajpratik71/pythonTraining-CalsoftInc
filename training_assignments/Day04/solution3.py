# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:42:48 2019

@author: pentela.srikrishna
"""

class Checking:
    def __init__(self, name):
        self.name = name
    def checking_the_object(self,name):
        self.name=name
obj = Checking("Calsoft")
obj.creating_the_object = "Calsoft.Inc"
print(obj.creating_the_object)
