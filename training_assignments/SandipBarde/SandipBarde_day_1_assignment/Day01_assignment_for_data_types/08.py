def UpdateValuesOfDictionary():
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    print("Dictionary values before update:- ", d)
    for i in d.keys():
        d[i] = d[i] + 10
    print("Updated dictionary values:- ", d)

if __name__ == "__main__":
    UpdateValuesOfDictionary()