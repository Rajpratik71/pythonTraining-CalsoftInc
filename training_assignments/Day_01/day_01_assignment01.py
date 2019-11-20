"""
1) Write a Python script with below functionality:
"""
#     a) It will have a function to generate Factorial of a number.
def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of {0} is :{1} ".format(n, fact))


# b) It will  have  a function to generate fibonacci series with count as number.
def Fibonacci(iteration):
        value1 = 0
        value2 = 1
        count = 0

        if iteration < 0:
            print("Please enter valid input")
        elif iteration == 1:
            print (  value1 )
        else:
            while count < iteration:
                print ( value1 ,end = ' ' )
                nth = value1 + value2
                value1= value2
                value2 = nth
                count = count + 1

"""
 c) Python script will take an input from the user of what function to perform.(Hint: Check input() and raw_input())
 d) The second input will be the number.
 e) Based on the number and function to be performed call the appropriate function and display the
    output to the user.
"""
if __name__ == "__main__":
    print ( "Enter Operation : \n1. Factorial")
    print("2. Fibbonoci")
    functionId = int( input("Enter function to perform : "))
    print(functionId)
    if functionId == 1:
        val = int(input("Enter value: "))
        print(val)
        print(Factorial(val))
    elif functionId == 2:
        val = int(input("Enter value: "))
        print(val)
        print(Fibonacci(val))
