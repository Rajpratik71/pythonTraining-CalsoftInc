a = int(input("enter first num"))
b = int(input("enter second num"))

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("divison by zero is done please change the second num")