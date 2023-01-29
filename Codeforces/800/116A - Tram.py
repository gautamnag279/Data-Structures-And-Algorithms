stops = int(input())
tram = [list(map(int, input().split(" "))) for i in range(stops)]
inTram = 0
max = 0

for i in range(stops):
    inTram -= tram[i][0]
    inTram += tram[i][1]
    if(inTram > max):
        max = inTram
print(max)
