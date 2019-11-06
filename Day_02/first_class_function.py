# Python program to illustrate functions
# can be treated as objects
def return_upper(text):
    return text.upper()


print(return_upper("Hello"))

new_func = return_upper

print(new_func("hola"))
#################################################


def upper_func(func):
    # storing the function in a variable
    greeting = func("Created by function passed as argument")
    print(greeting)


upper_func(return_upper)


# Python program to illustrate functions
# Functions can return another function


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
