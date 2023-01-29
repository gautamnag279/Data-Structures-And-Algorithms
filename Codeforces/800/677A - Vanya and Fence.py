n, wall = map(int, input().split(" "))
height = list(map(int, input().split(" ")))
count = 0

for i in height:
    if (i > wall):
        count += 2
    else:
        count += 1
print(count)
