"""dict operations"""

""" create dictionary using {} or dict()"""
d = {'company': 'calsoft', 'location': 'Bavdhan', 'other': {'employee': 800, 'offices': 4, 'MNC': True}}
print("value of d: ", d)

"""get the key,value from dictionary """
print("d['company']: ", d['company'])
print("d['other']['MNC']: ", d['other']['MNC'])
#print("d['name']: ", d['name'])          # keyError
print("d.get('name'): ", d.get('name'))   # return None if key is not found else returns value of key

"""get the keys/values or both from dictionary. d.keys() & d.values() provide list of keys, values respectively.
d.items() gives list of key,value tuples"""
print(f"d.keys(): {d.keys()}")
print(f"d.values: {d.values()}")
print(f"d.items: {d.items()}")

"""Update the key,value in the dictionary """
d['domain'] = 'storage & networking'  # update the value of a key
print("d['domain']: ", d['domain'])

# If key is not present in d, then will be added. If present in d, the corresponding value for that key is updated.
d.update({'floors': '8', 'location': 'SEZ'})
print("after updating: ", d)
d.pop('location', 'if key not found return this')
d.popitem() # will randomly remove and return k,v pair as tuple but raise keyerror if d is empty
del d['company'] # delete key company
print("after removing d['company']: ", d)
del d
#print(d) # Error
