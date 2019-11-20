def checker(func):
    def wrapper(*args):
        if(not args[0].isdigit()):
            print("Incorrect parameter passed.Please give an integer greater than zero")
            return
        elif(int(args[0]) < 0):
            print("Incorrect parameter passed.Please give an integer greater than zero")
            return
        if (not args[1].isdigit()):
            print("Incorrect parameter passed.Please give an integer greater than zero")
            return
        elif (int(args[1]) < 0):
            print("Incorrect parameter passed.Please give an integer greater than zero")
            return
        return (func(*args))
    return wrapper

@checker
def add(a,b):
    return (int(a)+int(b))

if __name__ == "__main__":
    a = input("Enter first number\n")
    b = input("Enter the second number")
    print(add(a,b))