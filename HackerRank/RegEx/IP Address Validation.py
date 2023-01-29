import re

for _ in range(0, int(input())):
    s = input()
    if re.match(r'^([1-2]?\d{1,2}\.){3}[1-2]?\d{1,2}$' , s):
        print("IPv4")
    elif re.match(r'^([a-f\d]{1,4}:){7}[a-f\d]{1,4}$', s):
        print('IPv6')
    else:
        print("Neither")
