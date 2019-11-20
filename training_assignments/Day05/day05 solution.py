# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:13:03 2019

@author: pentela.srikrishna
"""


lst=[1,2,3,4,-2,-4,-6]
sum=0
for i in lst:
    sum=sum+i
    for i in lst:
        if i==sum:
            print(i)
            break
