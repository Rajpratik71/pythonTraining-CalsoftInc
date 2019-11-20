# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:51:29 2019

@author: pentela.srikrishna
"""

def find_factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)
#factorial(int(input('enter the number')))
#ques2
def find_fibonacci(n):
    if n <= 0:
       return "Please enter positive integer."
    elif n == 1:
       return 0
    elif n == 2:
        return 1
    else:
        return find_fibonacci(n-1) + find_fibonacci(n-2)

if __name__ == '__main__':
   print("1: Generate Factorial")
   print("2: Generate Fibonacci series")
   choice = input("Enter operation to perform:")
   if choice == '1':
       fact=(find_factorial(int(input('enter the number'))))
       print(fact)
   elif choice == '2':
       count=find_fibonacci(int(input('enter fib series number')))
       print(count)
   else:
        print("Invalid selection! Please enter 1 or 2")
