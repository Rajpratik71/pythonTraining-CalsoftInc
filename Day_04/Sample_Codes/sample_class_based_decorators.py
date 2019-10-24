class SquareDecorator:

    # method which intializes the arguments of class(Constructor)
    def __init__(self, function):
        self.function = function

    # Main method of class based decorators where the function is executed
    def __call__(self, *args, **kwargs):
        print("Waiting for the function to be called")
        # Calling the function which is passed to the decorator and storing the return value in result
        result = self.function(*args, **kwargs)

        print("function called")
        return result


# adding decorator to the function
@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n


print("Square of number is:", get_square(195))
