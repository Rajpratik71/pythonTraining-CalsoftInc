def FiboSeries(num):
    a = 0
    b = 1
    c = a+b
    while a < num:
        yield c
        a = b
        b = c
        c = a+b




if __name__ == '__main__':
    num = int(input("please enter a number"))
    for i in FiboSeries(num):
        print(i)