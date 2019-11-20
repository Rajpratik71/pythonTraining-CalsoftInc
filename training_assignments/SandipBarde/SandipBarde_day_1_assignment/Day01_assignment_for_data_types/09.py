def CountListFromDictionary():
    d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'], "NonList":"this is not list"}
    count = 0
    print("Input Dictionary :- ", d)
    for i in d:
        if(type(d[i]) == list):
            count = count + 1
    return  count
print(CountListFromDictionary())