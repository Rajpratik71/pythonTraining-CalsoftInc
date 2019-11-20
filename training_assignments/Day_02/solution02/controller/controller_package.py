
import math
import random
class Math:
    def area_of_circle(radius):
        return (math.pi*(math.pow(radius,2)))
    def area_of_triagle(base,height):
        return ((base*height)/2)
    def area_of_rectangle(length,breadth):
        return(length*breadth)
    def area_of_square(side):
        return(math.pow(side,2))
class Random:
    def lucky_or_not(number,shufflenumber):
        numberlist=list(range(1,6))
        for number in range(shufflenumber):
            random.shuffle(numberlist)
        if numberlist[0]==number:
            return("you're lucky")
        else:
            return("you're not lucky")