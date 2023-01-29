import re

n = int(input())
reg = r'[a-zA-Z](?:\w+\.)*\w+@(?:\w+\.)+\w+'
l=[]
for i in range(n):
    l += re.findall(reg,input())

l = list(set(l))
l.sort()
print(";".join(l))
