def ConvertStringToListAndTuple(s):
    #accept string using input() function
    li = s.split(',')
    tu = tuple(li)
    print("List : ", li)
    print("Tuple : ", tu)

if __name__ == "__main__":
    s = input("Enter the comma-seperated numbers to convert into list and tuples \n")
    ConvertStringToListAndTuple(s)