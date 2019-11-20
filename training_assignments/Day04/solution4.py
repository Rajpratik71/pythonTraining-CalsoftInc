# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:43:20 2019

@author: pentela.srikrishna
"""

input1=int(input('enter the starting number'))
input2=int(input('enter the ending number'))
for i in range(input1,input2+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)