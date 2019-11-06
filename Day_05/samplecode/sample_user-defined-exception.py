# A python program to create user-defined exception

# class MyException is derived from super class Exception


class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg


def check_balance(bank_dict):
    for name, value in bank_dict.items():
        if value < 2000:
            raise MyException(f"balance amount is less in the account of {name}")


try:
    bank = {"Rajesh": 3000, "Naresh": 5000, "Ajay": 1800}
    check_balance(bank)
except MyException as me:
    print(me)
