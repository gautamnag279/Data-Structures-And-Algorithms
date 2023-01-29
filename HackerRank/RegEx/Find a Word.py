import re

s = ''
for i in range(int(input())):
    s += input() +' '

for i in range(int(input())):
    print(len(re.findall(r'((?<=\W)|^)%s((?=\W)|$)' % input(), s)))
