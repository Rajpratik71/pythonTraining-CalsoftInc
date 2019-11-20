class Person:
    def __init__(self, birthYear):
        self.birthYear = birthYear

    @classmethod
    def personByYear(cls, birthYear):
        cls.birthYear = birthYear
        return  cls(birthYear)

    @staticmethod
    def CheckPersonAge(self):
        if(self.birthYear < 1970):
            return "Person is adult"
        else:
            return "Person is not adult"


p = Person.personByYear(2016)
print(p.CheckPersonAge(p))
