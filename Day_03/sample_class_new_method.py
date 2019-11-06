#!/usr/bin/env python
"""
Program shows how Class and Object are work in Python
"""


class Employee:
    """
    Class Employee with employee name and pay details
    """

    # def __new__(cls, first, last, pay):
    #     print("Creating Instance")
    #     instance = super().__new__(cls)
    #     return instance

    def __new__(cls, first, last, salary):
        if 0 < salary < 11000:
            return object.__new__(cls)
        else:
            return None

    # Constructor
    def __init__(self, first, last, pay):
        """
        Initialize method
        :param first: Employee first name
        :param last: Employee last name
        :param pay: Employee salary
        """
        print("Initializing object")
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

    print(emp_1)
    print(emp_2)
