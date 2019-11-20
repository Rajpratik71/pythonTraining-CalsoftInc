# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:43:52 2019

@author: pentela.srikrishna
"""

a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1