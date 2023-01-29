import re

pattern = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'

for _ in range(0, int(input())):
    str = input()
    if re.match(pattern , str):
        print("VALID")
    else:
        print("INVALID")
