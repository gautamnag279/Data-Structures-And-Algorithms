import re

n = int(input())

for _ in range(n):
    if re.match("^[_.]{1}[0-9]{1,}[a-zA-Z]{0,}[_]{0,1}$",input()):
        print("VALID")
    else:
        print("INVALID")
