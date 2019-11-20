from datetime import date

class Person:
    def __init__(self,day,month,year ):
        self.date_of_birth = date(year,month,day)

    @classmethod
    def create_by_birthyear(cls,year):
        instance = cls(1,1,year)
        return instance

    @staticmethod
    def is_adult(dob):
        today  = date.today()
        years_diff = today.year - dob.year

        if(today.month < dob.month) or (today.month == dob.month and today.day < dob.day):
            years_diff = years_diff - 1

        if years_diff <= 18:
            return False
        else:
            return True




if __name__ == "__main__":
    person1 = Person(1,6,1990)
    person2 = Person.create_by_birthyear(1990)
    person3 = Person(28,1,2019)

    if Person.is_adult(person1.date_of_birth):
        print("Person1 is adult")
    else:
        print("Person1 is not adult")

    if Person.is_adult(person3.date_of_birth):
        print("Person3 is adult")
    else:
        print("Person3 is not adult")


       