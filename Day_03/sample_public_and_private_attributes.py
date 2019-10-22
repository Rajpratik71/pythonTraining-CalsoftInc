#!/usr/bin/env python
"""
Program on public, protected and private variables in python
"""


# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected
        self.__client = "ABC"

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.ccode)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        super().__init__(cName, proj)
        self.name = eName  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal)


if __name__ == "__main__":
    # creating instance of Company class
    c = Company("Stark Industries", "Mark 4")
    # creating instance of Employee class
    e = Emp("Steve", 9999999, c.name, c._proj)

    print(f"Welcome to {c.name}")
    # Employee(sub class) can access public and protected vars of Base class
    print(f"Here {e.name}, is working on {e._proj}")

    # to show the value of __sal we have created a public function show_sal()
    e.show_sal()

    # we can acces private variale as object._Class__var
    print(c._Company__client)
    print(e._Emp__sal)
