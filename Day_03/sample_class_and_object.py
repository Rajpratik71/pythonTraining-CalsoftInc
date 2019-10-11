class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'Fullname: {self.first} {self.last}'


emp_1 = Employee('Dnyaneshwar', 'Biradar', 10000)
emp_2 = Employee('Calsoft', 'Employee', 20000)
print(emp_1.fullname(), emp_2.fullname())