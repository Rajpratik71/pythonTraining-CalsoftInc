#!/usr/bin/env python
"""
Program shows how Class and Object are work in Python
"""


class Employee:
    """
    Class Employee with employee name and pay details
    """

    # Constructor
    def __init__(self, first, last, pay):
        """
        Initialize method
        :param first: Employee first name
        :param last: Employee last name
        :param pay: Employee salary
        """
        self.first = first
        self.last = last
        self.pay = pay

    # instance method
    def get_fullname(self):
        """
        Instance method to show full name of Employee
        :return: Full name of Employee
        """
        return f"Fullname: {self.first} {self.last}"

    # representation of object
    def __repr__(self):
        """
        Magic method for representational format of object
        :return: reprasentation in 'First - Last' name
        """
        return f"Representation: {self.first} - {self.last}"


if __name__ == "__main__":
    # creating object of Employee class
    emp_1 = Employee("John", "Lee", 10000)
    emp_2 = Employee("David", "Smith", 20000)

    # instance method call
    print(emp_1.get_fullname())
    print(emp_2.get_fullname())

    # using repr we can have representation of object when we print
    print(emp_1)
    print(emp_2)

    # Type of object
    print(type(emp_1))

    # Checking object belongs to which class
    if isinstance(emp_1, Employee):
        print("Employee object")
    else:
        print("Non employee")

    # memory locations for each object
    print(id(emp_1), id(emp_2))

    # Documentation string(Doc string)
    print("Doc string", emp_1.__doc__)
    print(help(emp_1))
