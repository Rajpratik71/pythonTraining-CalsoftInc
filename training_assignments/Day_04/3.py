class Checking:
    checking_the_object = True
    creating_the_object = ''
    def __init__(self, name):
        self.name = name

obj = Checking("Calsoft")
print(obj.checking_the_object)
obj.creating_the_object = "Calsoft.Inc"
print(obj.creating_the_object)
