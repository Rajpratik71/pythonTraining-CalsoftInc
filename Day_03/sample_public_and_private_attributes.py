class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.__pay = pay

    def fullname(self):
        return f'Fullname: {self.first} {self.last}'

    def __salary_details(self):
        return self.__pay

emp_1 = Employee('Dnyaneshwar', 'Biradar', 10000)
emp_2 = Employee('Calsoft', 'Employee', 20000)
print(emp_1.fullname(), emp_2.fullname()) #public

# print(emp_1.__pay) #Attribute error
# print(emp_1.__salary_details) #Attribute error

print(emp_1._Employee__pay)
print(emp_2._Employee__salary_details())