number_of_children, transform_time = map(int, input().split(" "))
queue = list(input())

for j in range(0, transform_time):
    i = 0
    while(i < number_of_children - 1):
        if(queue[i] == "B" and queue[i+1] == "G"):
            queue[i] = "G"
            queue[i+1] = "B"
            i += 1
        i += 1
print("".join(queue))
