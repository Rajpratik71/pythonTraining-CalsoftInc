class A:
     def check_in_class(self):
         print("I am in class A")


def check_in_func(self):
    print("I am in function")


# Replacing or Patching check_in_class with check_in_func in runtime
A.check_in_class = check_in_func
obj = A()
obj.check_in_class()
