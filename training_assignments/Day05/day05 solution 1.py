# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:35:46 2019

@author: pentela.srikrishna
"""

num = int(input("enter a number: "))
 
length = len(str(num))
add = 0
temp = num
 
while(temp != 0):
	add = add + ((temp % 10) ** length)
	temp = temp // 10
 
if add == num:
	print("armstrong number")
else:
	print("not armstrong number")
    





    

