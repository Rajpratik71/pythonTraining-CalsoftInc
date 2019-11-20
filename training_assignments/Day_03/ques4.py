from abc import ABC, abstractmethod
class AbstractOperation(ABC):

    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def operation(self):
        pass

class Add(AbstractOperation):

    def __init__(self, o1, o2):
        super().__init__(o1, o2)

    def operation(self):
        return self.o1+self.o2

class Sub(AbstractOperation):

    def __init__(self, o1, o2):
        super().__init__(o1, o2)

    def operation(self):
        return self.o1-self.o2

class Mul(AbstractOperation):

    def __init__(self, o1, o2):
        super().__init__(o1, o2)

    def operation(self):
        return self.o1*self.o2

class Div(AbstractOperation):

    def __init__(self, o1, o2):
        super().__init__(o1, o2)

    def operation(self):
        return self.o1/self.o2

if __name__ == '__main__':

    add = Add(1, 2)
    print(add.operation())

    sub = Sub(1, 2)
    print(sub.operation())

    mul = Mul(1, 2)
    print(mul.operation())

    div = Div(1, 2)
    print(div.operation())
