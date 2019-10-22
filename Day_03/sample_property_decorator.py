#!/usr/bin/env python
"""
Program on property decorators in Python
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


if __name__ == "__main__":
    emp = Employee("John", "Smith")
    print(emp.first, emp.last)
    # property getter call
    print(f"Full name 1: {emp.fullname}")

    # property setter call
    emp.fullname = "Dan Smith"
    print(f"Full name 2: {emp.fullname}")
    print(emp.first, emp.last)

    # property  deleter call
    del emp.fullname
    print(f"Deleted Full name: {emp.first} {emp.last}")
