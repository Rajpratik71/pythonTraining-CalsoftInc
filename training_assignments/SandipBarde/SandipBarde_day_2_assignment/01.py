def func(*args, li = []):
    for arg in args:
        li.append(arg)
    print(li)

if __name__ == "__main__":
    func(1, 2, 3)
    a = []
    func([1, 3,4], a)
    func(8,9,10)


"""
Observations

In background it matching the argument with the function defination arguments.
If we just provide list then it's mapping as list argument and mapping to *args can be null(not argument provided)
If we just provide the variable number of argument each argument is matched if it's list type.
    In this case we have two situations
        1 - first argument is list - It's directly mapping with list argument and map *args as null and giving error to arguments after first agrument.
        2 - first argument is not list - All argumets before the list arguments are mapped to *args and list agrument is match with last argument.
While passing list as func(7,8,9, a=[]) giving error because of variable name does not match with defination variable name.
If we pass list as func(7,8,9, li=[]) works as name of variable pass and name of defination variable matched.

"""