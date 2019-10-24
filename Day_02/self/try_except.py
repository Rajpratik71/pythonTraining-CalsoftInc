def divide(x, y):
    try:
        result = x // y
        print("Floor division is done . And your result is ", result)
    except ZeroDivisionError:
        print(" Sorry division by Int is allowed ")


divide(3, 2)
