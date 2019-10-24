# Single expect statement
arr = [1, 2, 3]

try:
    print("Second Element : " + str(arr[1]))

    print("Second Element :" + str(arr[3]))

except IndexError:
    print("No Element at that index")
