rows = int(input())
count = 0
for i in range(rows):
    lst = list(map(int, input().split()))
    if (lst.count(1) >= 2):
        count += 1
print(count)
