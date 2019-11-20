


def fac(num):
    """
    function for finding the factorial of a number
    """
    f=1
    if  num < 0:
        print("negative number not allowed")
    elif num == 0:
        print(1)
    else:
        for i in range(1,num+1):
            f = f*i
        print(f)    

def fib(num):
    """
    function to print the fibonacci series upto that number 
    """
    a=0
    b=1
    if num < 0:
        print("negitive number")
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c)
    

if __name__=='__main__':
    
    choice=int(input("1. factorial  2.fibonacci series"))
    num=int(input("please enter a number"))
    if choice == 1:
        fac(num)
    elif choice == 2:
        fib(num)

