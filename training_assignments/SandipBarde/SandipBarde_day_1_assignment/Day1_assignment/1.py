def Fact(x):
    if(x==0):
        return 1
    return x * Fact(x-1)
def GererateFibo(x):
    if(x==1) :
        return [1]
    if(x==2):
        return [1,1]
    first = 1
    second = 1
    li = []
    li.append(1)
    li.append(1)
    while((x - 2) != 0):
        third = first + second
        first = second
        second = third
        li.append(third)
        x = x - 1
    return li

if __name__ == "__main__":
    print("Enter option to perform operation")
    print("1 - Factorial of number")
    print("2 - Print fibonacci series upto given number")
    choice = int(input())
    if choice == 1 :
        print("Eneter the number")
        print(Fact(int(input())))
    elif choice == 2 :
        print("Eneter the number")
        print(GererateFibo(int(input())))
    else:
        print("Please enter correct option")
        exit(0)


