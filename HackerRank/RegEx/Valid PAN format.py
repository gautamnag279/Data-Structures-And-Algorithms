import re

pattern = r'^[A-Z]{5}\d{4}[A-Z]$'

for _ in range(0, int(input())):
    s = input()
    if re.search(pattern , s):
        print('YES')
    else:
        print('NO')
