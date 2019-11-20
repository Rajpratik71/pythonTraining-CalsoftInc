# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:25:57 2019

@author: pentela.srikrishna
"""

class NegativePriceException(Exeption):
    def __init__(self,msg):
        self.msg=msg
    def check_native(price):
        if price < 0:
            raise NegativePriceException("Price can not be negative")
if __name__=='__main__:
      price = int(input("Enter integer number"))
      try:
             check_native(price):          
      excepton NegativePriceException as price:
          print(price)