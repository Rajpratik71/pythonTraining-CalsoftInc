# the main function takes another function as a parameter
def make_pretty(func):
    # the inner function takes those arguments which needs to be passed to the decorated function
    def inner(name, age):
        print("I got decorated")
        # calling the function which is decorated
        func(name, age)
    return inner


@make_pretty
def ordinary(name, age):
    print("I am ordinary")
    print("My name is {}".format(name))
    print("My age is {}".format(age))


ordinary('Dawood', '25')
