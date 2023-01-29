n = int(input())
magnet = [input() for i in range(n)]
count = 0

for i in range(n-1):
    if (magnet[i] != magnet[i+1]):
        count += 1

print(count + 1)
