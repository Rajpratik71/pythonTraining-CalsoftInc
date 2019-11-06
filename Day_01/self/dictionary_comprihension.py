# Python Code to demonstrate dictionary Comprihensation

keys = ["a", "b", "c", "d", "e"]

# values = [1,2,3,4,5]

values = range(1, 6)

myDict = {k: v for (k, v) in zip(keys, values)}

print(myDict)

print(" Another way using zip function")

mynewDict = dict(zip(keys, values))

print(mynewDict)

# Dictionary using List Comprwehension

myListDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}

print("Created Dict using List Comprehensation")

print(myListDict)

mytestDict = {x.upper(): x * 3 for x in "coding"}

print(mytestDict)
