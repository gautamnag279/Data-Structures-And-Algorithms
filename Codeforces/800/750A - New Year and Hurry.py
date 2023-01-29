questions, journey = map(int, input().split(" "))
time = 240 - journey
count = 0
total = 0
for i in range(1, questions + 1):
    total += i*5
    if (total <= time):
        count += 1
print(count)
