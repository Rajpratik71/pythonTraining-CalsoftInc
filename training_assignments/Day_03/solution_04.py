# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:04:57 2019

@author: vamsi.reddy
"""
from abc import ABC, abstractmethod
class AbstractOperation(ABC):
    @abstractmethod
    def __init__(self,operand1,operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    @abstractmethod
    def operation(self):
        pass
class Subtraction(AbstractOperation):
    def __init__(self,operand1,operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    def operation(self):
        return(self.operand1-self.operand2)
class Addition(AbstractOperation):
    def __init__(self,operand1,operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    def operation(self):
        return(self.operand1+self.operand2)
class Multiplication(AbstractOperation):
    def __init__(self,operand1,operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    def operation(self):
        return(self.operand1*self.operand2)
if __name__ == '__main__':
    Add_obj = Addition(5,6)
    Sub_obj = Subtraction(5,6)
    Multi_obj = Multiplication(5,6)
    print('Addition of {} and {} is {}'.format(Add_obj.operand1,Add_obj.operand2,Add_obj.operation()))
    print('Subtraction of {} and {} is {}'.format(Sub_obj.operand1,Sub_obj.operand2,Sub_obj.operation()))
    print('Multiplication of {} and {} is {}'.format(Multi_obj.operand1,Multi_obj.operand2,Multi_obj.operation()))
