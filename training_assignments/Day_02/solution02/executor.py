# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:04:43 2019

@author: vamsi.reddy
"""
from controller import controller_package
print("Hi, I'm executor \n I can tell you the areas of shapes and I can also play a game with you")
option = int(input('choose 1 for finding areas of shapes and 2 for playing game'))
if option==1:
    print("all the dimensions in cm")
    shape= int(input('Choose shape 1 FOR  CIRCLE\n 2 FOR TRIANGLE\n 3 FOR RECTANGLE\n 4 FOR SQUARE'))
    if shape ==1:
        radius = (int(input('give radius of circle')))
        print(controller_package.Math.area_of_circle(radius))
    elif shape ==2:
        width = (int(input('give base of triangle')))
        height = (int(input('give height of triangle')))
        print(controller_package.Math.area_of_triagle(height,width))
    elif shape ==3:
        length = (int(input('give length of rectangle')))
        breadth = (int(input('give breadth of rectangle')))
        print(controller_package.Math.area_of_rectangle(length,breadth))
    elif shape ==4:
        side = (int(input('give length of side of square')))
        print(controller_package.Math.area_of_square(side))   
    else:
        print('please choose correct option')
elif option==2:
    print("\n\nThis is guessing game which decides weather you're lucky or not")
    print("I will ask you a number to choose between 1-5 including both 1 and 5")
    print("I will ask you the number of times to shuffle the list of numbers from 1 to 5")
    print("If the first number in shuffled list is same as the number you choose then you're lucky" )
    number=(int(input("let's start the game. choose a number from 1-5")))
    shufflenumber=(int(input("choose the number of times the list to be shuffled")))
    print(controller_package.Random.lucky_or_not(number,shufflenumber))
else:
    print('choose the correct option')