n = int(input())
jersey1 = []
jersey2 = []
count = 0

for i in range(n):
    a, b = map(int, input().split(" "))
    jersey1.append(a)
    jersey2.append(b)

for i in range(n):
    for j in range(n):
        if(jersey1[i] == jersey2[j]):
            count += 1
print(count)
