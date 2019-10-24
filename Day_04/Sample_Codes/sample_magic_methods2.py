class Employee:

    # Magic method which is always called when trying to get an attribute which is not present in class
    def __getattr__(self, item):
        print("__getattr__ called")
        return item.upper()

    # Magic method which is always called when setting a value to an attribute which is not present in the class
    def __setattr__(self, name, value):
        print("__setattr__ called")
        self.__dict__[name] = value.upper()


obj = Employee()
# Calling an attribute which is not present so it will call __getattr__
print(obj.does_not_exist)

# Setting a value to an attribute which is not present so it will call __setattr__
obj.person = 'Dawood'
print(obj.person)
