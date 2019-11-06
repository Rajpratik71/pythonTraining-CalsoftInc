def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x - 1)


num = input("Please input the Number : ")

print("The factorial of num", num, "is", calc_factorial(int(num)))
