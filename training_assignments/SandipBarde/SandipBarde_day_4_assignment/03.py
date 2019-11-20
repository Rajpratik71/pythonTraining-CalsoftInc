class Checking:
    def __getattr__(self, item): # if we call attribute on object where attribute does not exits it will call this method.
        return item.upper()
    def __init__(self, name):
        self.name = name

obj = Checking("Calsoft")
print(obj.checking_the_object) # this will result into error "checking_the_object" if we have not defined __getattr__ method
obj.creating_the_object = "Calsoft.Inc"
print(obj.creating_the_object)
