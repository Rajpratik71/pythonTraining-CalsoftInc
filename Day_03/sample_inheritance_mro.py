class A(object):
    def who_am_i(self):
        print("I am a A")
        # super().who_am_i()


class B(A):
    def who_am_i(self):
        print("I am a B")
        super().who_am_i()


class C(A):
    def who_am_i(self):
        print("I am a C")
        super().who_am_i()


class D(B,C): # order change, mro will change
    def who_am_i(self):
        print("I am a D")
        super().who_am_i()

d1 = D()
d1.who_am_i()
print(D.__mro__)
print(D.mro())