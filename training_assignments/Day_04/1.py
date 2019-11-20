class Num:

    def __init__(self, num1):
        self.num1 = num1

    def __sub__(self, num2):
        return self.num1-num2

if __name__=='__main__':
    num = Num(5)
    print(num-3)