import re

n = int(input())

Reg = r"\([+\-]?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), [+\-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{2}(\.\d+)?|\d(\.\d+)?)\)"

for _ in range (n):
    p = input()
    if re.match(Reg, p):
        print('Valid')
    else:
        print('Invalid')
