from itertools import count


limak, bob = map(int, input().split(" "))
years = 0
while(limak <= bob):
    limak *= 3
    bob *= 2
    years += 1
print(years)
