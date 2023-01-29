import re

pattern = r'.*hackerrank'
count = 0

for _ in range(0, int(input())):
    str = input()
    if re.match(pattern , str.lower()):
        count = count + 1
print(count)

