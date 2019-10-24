class Callable():
     def __call__(self, *args, **kwargs):
         print("Inside the call method")
         self.check_method()
     def check_method(self):
         print("Inside the check method")


obj = Callable()
obj()
