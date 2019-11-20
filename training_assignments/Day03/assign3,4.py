
   # -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:53:33 2019

@author: venkata.ramaiah
"""
from abc import ABC, abstractmethod
class Abstractmethod(ABC):
    @abstractmethod
    def __init__(self,operand1,operand2):
        self.operand1=operand1
        self.operand2=operand2
    def operation(self):
        return None
    
class  add(Abstractmethod):
     
    def __init__(self,operand1,operand2):
        super().__init__(operand1,operand2)
    def operation(self):
        return self.operand1+self.operand2
  
class sub(Abstractmethod):
    
        def __init__(self,operand1,operand2):
            super().__init__(operand1,operand2)
            
        def operation(self):
            return (self.operand1 - self.operand2)
        
class mul(Abstractmethod):
    
    def __init__(self,operand1,operand2):
        super().__init__(operand1,operand2)
             
    def operation(self):
            return (self.operand1 *self. operand2)
         
if __name__=='__main__':
   a1=add(1,2)
   print(a1.operation())
   a2=sub(1,2)
   print(a2.operation())
   a3=mul(1,2)
   print(a3.operation())
   
   
