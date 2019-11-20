import re

result = re.findall(r"th", "the python training")
result = re.findall("\w", "the python training")

print(result)
