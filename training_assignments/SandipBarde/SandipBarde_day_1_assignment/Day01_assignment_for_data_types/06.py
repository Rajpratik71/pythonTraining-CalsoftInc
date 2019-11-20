def FindSecondLargestInList():
    li = [-8, 1, 2, -2, 0]
    print("Input List", li)
    m = max(li)
    li.remove(m)
    sM = max(li)
    print("Second max Element : ", sM)

if __name__ == "__main__":
    FindSecondLargestInList()