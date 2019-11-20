class AddComplex:
    def __init__(self, complexnum):
        self.complexnum = complexnum

    def __add__(self, other):
        return (self.complexnum + other.complexnum)

if __name__ == '__main__':
    c1 = AddComplex(1+2j)
    c2 = AddComplex(2+1j)
    print(c1+c2)