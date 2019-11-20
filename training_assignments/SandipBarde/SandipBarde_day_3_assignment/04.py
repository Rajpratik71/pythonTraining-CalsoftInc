from  abc import ABC, abstractmethod
class AbstractClass(ABC):
    #@abstractmethod
    def doOperation(self, a, b):
        pass

class AddClass(AbstractClass):
    def __init__(self):
        pass
    def doOperation(self, a, b):
        return a + b

class SubClass(AbstractClass):
    def doOperation(self, a, b):
        return a - b

class MulClass(AbstractClass):
    def doOperation(self, a, b):
         return a * b
    def __init__(self):
        pass

a = MulClass()
print(a.doOperation(3,4))


