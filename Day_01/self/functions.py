# Function to illustrate break in loop


def breaktestfun(arr):
    for i in arr:
        if i == 5:
            break
            print("function demonstrating breaktestfun")
        print(i)

    print()


def continuetestfun(arr):
    for i in arr:
        if i == 5:
            continue
            print("function demonstrating continuetestfun")
        print(i)
    print()


def passtestfun(arr):
    print("Function demonstrating pass fuction")
    pass


arr = [1, 2, 3, 4, 5, 6, 7, 8]

print("function demonstrating breaktestfun")
breaktestfun(arr)

print("function demonstrating continuetestfun")
continuetestfun(arr)

print("function demonstrating passtestfun")
passtestfun(arr)
