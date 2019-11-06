test_list = [{"gfg": 2, "is": 4, "best": 6}, {"it": 5, "is": 7, "best": 8}, {"CS": 10}]

print("The original list is : " + str(test_list))

result = {}

for sub in test_list:
    for key, val in sub.items():
        result.setdefault(key, []).append(val)

print("The merged values encapsulated dictionary is : ", result)
