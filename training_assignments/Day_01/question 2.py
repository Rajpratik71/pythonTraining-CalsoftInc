# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:26:12 2019

@author: venkata.ramaiah
"""
####  Question number 3  #############
def file():
    with open("rams.txt",'w') as f:
        f.write("hello good morning")
    with open("rams.txt",'r') as f:
        reading=f.read()
        print(reading)
if __name__=='__main__':  
    file()
##########################################       




########### Qestion  No (2) #####################

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
######################################################


