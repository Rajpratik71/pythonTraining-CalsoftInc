from datetime import datetime,date
class Person:

    def __init__(self,date,month,year):
        self.date  = date
        self.month = month
        self.year  = year

    @classmethod
    def age_m(cls,date):
        year, month, date = date.split('-')
        return cls(date,month,year)


    @staticmethod
    def check_adult(by):
        year, month, day = by.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        current_date = datetime.today()
        b1 = date(current_date.year, current_date.month, current_date.day)
        b2 = date(year, month, day)
        check_bd=(b1-b2).days
        return (check_bd/365)

if __name__=='__main__':
    obj = Person.age_m('2018-09-09')
    print(obj)
    current_age = Person.check_adult('1998-07-18')
    if(current_age >= 18):
        print("Person is adult")
    else:
        print("Person is not adult")