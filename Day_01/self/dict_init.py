# Dictionary with multiple key

test_dict = {}

test_keys = {'abc', 'def' , 'ghi'}

for keys in test_keys:
    test_dict[keys] = 4

print("Dictionary after updating " + str(test_dict))