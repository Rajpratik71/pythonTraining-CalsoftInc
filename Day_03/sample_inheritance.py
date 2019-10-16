#!/usr/bin/env python
"""
Program on inheritance in Python using Employee, Developer and Manager class
"""


# Base class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_fullname(self):
        return f"{self.first} {self.last}"


# sub class
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # calls base class constructor
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return str(self.get_fullname())


# sub class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=[]):
        super().__init__(first, last, pay)
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        # if emp in self.employees:
        self.employees.remove(emp)


if __name__ == "__main__":
    dev_1 = Developer("David", "Gelvin", 50000, "Python")
    dev_2 = Developer("Test", "Employee", 60000, "Java")

    # Inherited method call for dev1
    print(dev_1.get_fullname())
    mgr_1 = Manager("Dan", "Smith", 70000, [dev_1, dev_2])

    mgr_1.add_emp(dev_1)
    mgr_1.add_emp(dev_2)

    for employee in mgr_1.employees:
        print("Manager hold employee:", employee)

    mgr_1.remove_emp(dev_2)

    for employee in mgr_1.employees:
        print("After deletion:", employee)
