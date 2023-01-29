rooms = int(input())
count = 0
for i in range(rooms):
    living, capacity = map(int, input().split(" "))
    if(capacity - living >= 2):
        count +=1 
print(count)
