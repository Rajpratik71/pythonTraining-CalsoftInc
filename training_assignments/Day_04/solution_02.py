def func(comp):
    if '+' in comp:
        lst = comp.split('+')
    else:
        lst = comp.split('-')
    a=int(lst[0])
    i=int(lst[1][:-1])
    return(a,i)


class Complex:
    def __init__(self,args):
        self.a=args[0]
        self.i=args[1]
    def __add__(obj1,obj2):
        return('{}+{}j'.format(obj1.a+obj2.a,obj1.i+obj2.i))
input1 = input('Give 1st complex number')
input2 = input('Give 2nd complex number')
obj1 = Complex(func(input1))
obj2 = Complex(func(input2))
Complex.__add__(obj1,obj2)