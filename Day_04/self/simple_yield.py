# Basic Uses of yield under Python Generators

def simpleGeneratorFun():
    for i in range(10):
        i += i
        yield i
    yield i

for value in simpleGeneratorFun():
    print(value)