def outer_foo():
    outer_var = 3

    def inner_foo():
        inner_var = 5
        print (dir(), " - names in inner_foo")
        # Uncomment the below function and check the output again
        # print(outer_var)

    outer_var = 7
    inner_foo()
    print (dir(), " - names in outer_foo")


outer_foo()


def f():
    print s

    # This program will NOT show error
    # if we comment below line.
    s = "defining in function"

    print s


# Global scope
s = "in global scope"
# Uncomment below line to check the exception
# f()
print s
