import pdb

lst = list(map(int,input().split()))
neg=pos=0
for num in lst:
    if num<0:
        neg = neg+1
    else:
        pos = pos+1
    pdb.set_trace()
print(neg,pos)