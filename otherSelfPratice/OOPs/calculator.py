class CalC():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        '''
        Add method
        :return: addition of numbers
        '''
        return self.num1 + self.num2

    def sub(self):
        '''
        Substract  method
        :return: substraction of numbers
        '''
        return self.num1 - self.num2

    def mul(self):
        '''
        Multiply method
        :return: multiplication of numbers
        '''
        return self.num1 * self.num2

    def div(self):
        '''
        Divide method
        :return: division on numbers
        '''
        if not isinstance(self.num1, (int, float)) or not isinstance(self.num2, (int, float)):
            return 'Type error'
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return 'Dividing by Zero is not allowed'


calcObj = CalC(0, 10)
print('Addition is: ', calcObj.add())
print('Substraction is:', calcObj.sub())
print('Multiplication is:', calcObj.mul())
print('Division is: ', calcObj.div())
