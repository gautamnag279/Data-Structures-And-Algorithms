guest = input()
host = input()

ordered = sorted((guest + host))
pile = sorted(input())

if(ordered == pile):
    print("YES")
else:
    print("NO")
