# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:54:08 2019

@author: pentela.srikrishna
"""

s="abcdef"
print(s[ ::2])

user=input()
res = list(map(str, user.split(',')))
tu=tuple(res)
print(res)
print(tu)



user=input()
st=user[user.index['p']:]
print(st)

user=list(input())
#print(user)
#res = list(map(int, user.split(',')))
#print(res)
k=['a','e','i','o','u']
l=[]
for i in user:
    if i in k:
        l.append(i)
print(len(l))
        

inputt=[1,3,1,'java','python','python']
s=set(inputt)
s=list(s)
print(s)


v=[8, 1, 2, 2, 0]
print(v.sort())
print(l)
print(l[-1])


v=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#for i in v:
v[1][2]=100
print(v)