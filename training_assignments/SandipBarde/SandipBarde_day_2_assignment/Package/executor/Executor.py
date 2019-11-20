from controller import Controller as mop

if __name__ == "__main__":
    choice = 0
    print("Enter choice for operation to be perform")
    print("1 - square of number")
    print("2 - cube of number")
    print("3 - square root of number")
    print("4 - factorial of number")
    print("5 - GCD of two numbers")
    choice = int(input())
    if(choice == 1) :
        x = int(input("Enter the number\n"))
        print("Square of given number :- ", mop.square(x))
    elif(choice == 2):
        x = int(input("Enter the number\n"))
        print("Cube of given number :- ", mop.cube(x))
    elif(choice == 3):
        x = int(input("Enter the number\n"))
        print("Square root of given number :- ", mop.sqrt(x))
    elif (choice == 4):
        x = int(input("Enter the number\n"))
        print("Factorial of given number :- ", mop.fact(x))
    elif (choice == 5):
        x = int(input("Enter the first number\n"))
        y = int(input("Enter the second number\n"))
        print("GCD of given numbers :- ", mop.gcd(x,y))
    else:
        print("Please choice option from available options")
