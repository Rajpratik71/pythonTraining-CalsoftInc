
def RemoveDuplicateFromList():
    li = [1, 3, 1, 'python', 'java', 'python']
    print("Original list: ", li)
    resultList = []
    eset = set() # created empty set
    for item in li:
        eset.add(item)
    for item in eset:
        resultList.append(item)
    print("Result List after remove duplicate: ", resultList)

if __name__ == "__main__":
    RemoveDuplicateFromList()