class MagicMethodDemo:
    def __init__(self, num):
        self.num = num

    # when we substract from the class object this method will get called.
    def __sub__(self, other):
        return self.num - other

obj = MagicMethodDemo(100)
# If we do not implement __sub__ method for the class MagicMethod demo below substraction will not work.
# Will result into error operand type error.
print(obj-50) # this will call tho __sub__ method and will return 50.