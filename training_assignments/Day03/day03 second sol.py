# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:21:26 2019

@author: pentela.srikrishna
"""

from datetime import date
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method 
    @staticmethod
    def isAdult(age): 
        return age > 18
p1=person('ram',22)
p2=person.fromBirthYear('ramakrishna',1997)

print(p1.age)
print(p2.age)
print(person.isAdult(22))
