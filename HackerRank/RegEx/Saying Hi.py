import re

for _ in range(0, int(input())):
    s = input()
    
    if re.search(r'^[Hh][Ii]\s[^Dd]\w*', s):
        print(s)
    else:
        pass
