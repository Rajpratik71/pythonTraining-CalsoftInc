import pdb
l1 = [1, 2, 3, -1, -3]
pc = 0
nc = 0

pdb.set_trace()
for i in l1:
    if i >= 0:
        pc = pc+1
    else:
        nc = nc+1

print(f"postive counts {pc}")
print(f"negitive counts {nc}")