
def ModifyTupleOfList():
    newLi = []
    li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    for index in range(len(li)):
        templist = []
        for i in li[index]:
            print(i)
            templist.append(i)
        templist[len(templist)-1] += 100
        newLi.append(tuple(templist))
    return newLi
if __name__ == "__main__":
    print(ModifyTupleOfList())