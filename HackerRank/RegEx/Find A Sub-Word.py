import re

string = ''
for i in range(int(input())):
    string += input() + ' '

for i in range(int(input())):
    print(len(re.findall(r'(\w)'+input()+'(\w)',string)))
