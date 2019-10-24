import re

pattern = '^tes...t$'
test_string = 'testtttttesttttesttttestttestttestttesttetsttestttt'

# Very basic , not so efficient

result = re.match(pattern, test_string)
if result:
    print('Search Succssfull')
else:
    print('Search Unsucessfull')