#!/usr/bin/env python
"""
Program on class method and static method in Python
"""
import datetime
import typing


class Employee:
    """
    Class Employee that illustrate method types in class
    """

    # class variable
    raise_amt = 1.04

    # constructor
    def __init__(self, first, last, pay) -> None:
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
    def get_fullname(self) -> str:
        """
        Instance method to show full name of Employee
        :return: Full name of Employee
        """
        return f"Fullname: {self.first} {self.last}"

    @classmethod
    def set_raise_amt(cls, amount: int) -> int:
        """
        Class method to change class variable raise amount
        """
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str: str) -> None:
        """
        Class method which takes string and act as alternative constructor
        """
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day: datetime) -> bool:
        """
        Helper method to show whether a day is weekday or weekend
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == "__main__":
    emp_1 = Employee("David", "Smith", 50000)
    emp_2 = Employee("John", "Lee", 60000)

    # Instance method call
    print(emp_1.get_fullname())

    # Class method call
    Employee.set_raise_amt(1.05)

    print(Employee.raise_amt)
    print(emp_1.raise_amt)
    print(emp_2.raise_amt)

    emp_str_1 = "John-Doe-70000"
    emp_str_2 = "Steve-Smith-30000"
    emp_str_3 = "Jane-Doe-90000"

    first, last, pay = emp_str_1.split("-")

    # Class method call
    new_emp_1 = Employee.from_string(emp_str_1)

    print(new_emp_1.first, new_emp_1.last, new_emp_1.pay)

    my_date = datetime.date(2016, 7, 11)
    # static method call
    print(Employee.is_workday(my_date))

    # typing module usage
    print(typing.get_type_hints(emp_1.get_fullname))
    print(typing.get_type_hints(Employee.is_workday))
