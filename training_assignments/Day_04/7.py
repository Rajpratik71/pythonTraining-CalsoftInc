def decorator(func):
    def wrapper():
        print("I am the decorator")
        func()
    return wrapper

@decorator
def function():
    print("I am the function")
function()
