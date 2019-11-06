class Employee:

    does_not_exist = "I am present"

    def __getattr__(self, item):
        print("__getattr__ called")
        return item.upper()

    def __getattribute__(self, item):
        print("__getattribute__ called")
        return item.split("_")


obj = Employee()
print(obj.does_not_exist)
