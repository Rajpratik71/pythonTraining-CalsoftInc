class ABC:
    def AddSub(self, a, b):
        print(a+b)

def SubAdd(a, b):
    print(a-b)

abc = ABC()
abc.AddSub(1,2)
abc.AddSub = SubAdd
abc.AddSub(2,3)