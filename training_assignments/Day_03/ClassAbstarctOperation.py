
from abc import ABC, abstractmethod

class AbstractOperation(ABC):

    def __init__(self,operand1, operand2):
        self.op1 = operand1
        self.op2 = operand2

    @abstractmethod
    def operation(self):
        return None



class Addition(AbstractOperation):

    def __init__(self,op1,op2):
        super().__init__(op1,op2)


    def operation(self):
        return self.op1 + self.op2

class Subtraction(AbstractOperation):

    def __init__(self,op1,op2):

        super().__init__(op1,op2)


    def operation(self):
        return self.op1 - self.op2


class Multiplication(AbstractOperation):

    def __init__(self,op1,op2):

        super().__init__(op1,op2)


    def operation(self):
        return self.op1 * self.op2


if __name__ == "__main__":

    add = Addition(5,5)
    subtract = Subtraction(10,5)
    multiply = Multiplication(5,5)

    print("Addition of {} and {} is {}".format(add.op1,add.op2,add.operation()))
    print("Subtraction of {} and {} is {}".format(subtract.op1,subtract.op2,subtract.operation()))
    print("Multiplication of {} and {} is {}".format(multiply.op1,multiply.op2,multiply.operation()))
