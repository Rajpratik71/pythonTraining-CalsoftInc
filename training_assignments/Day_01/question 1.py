# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:53:43 2019

@author: venkata.ramaiah
"""
#########Day one Assingment Question 1 #############
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1) 
    
def fibonacci(num):
    if num <= 0:
     print("incorrect")
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibonacci(num-1)+(num-2) 
print(fibonacci(66))    
if __name__=='__main__':
    user1=int(input("enter the yur condition::\n\n 1.fact\n\n 2.fibon\n"))
    if(user1==1):
        user=int(input("enter the number to perform task:"))
        fact1=fact(user)
        print(fact1)
    elif(user1==2):
         count=int(input("enter count to perform fibonacci series:"))
         fibonacci1=fibonacci(count)
         print(fibonacci1)

################################################################