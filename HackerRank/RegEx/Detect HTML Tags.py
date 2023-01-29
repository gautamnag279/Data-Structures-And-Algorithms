import re

N = int(input())

res = []

for _ in range(N):
    res += re.findall('<(\s*?\w+\s*?)', input())

print(';'.join(sorted(set(res))))
