# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:59:44 2019

@author: venkata.ramaiah
"""
########### Qestion  No  2 #####################

import samplelib
def get_all_prime(limit):
    i = 2  
    while limit > 0:
        if samplelib.is_prime(i):
           limit = limit - 1
           print(i)
        i = i+1
if __name__ == "__main_": 
    count = int(input("Enter count of prime numbers:"))
    
    get_all_prime(count)
############## END  ########################################
