class Sub_of_int:
    def __init__(self,number1):
        self.number1 = number1
    def __sub__(self,number2):
        return(self.number1-number2)
        print('subtracting')
if __name__ == '__main__':      
    number1 = Sub_of_int(5)
    print(number1 - 3)