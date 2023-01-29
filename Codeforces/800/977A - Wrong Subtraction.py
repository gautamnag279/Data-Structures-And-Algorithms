num, steps = map(int, input().split(" "))
while(steps > 0):
    if(num % 10 == 0):
        num = num//10
    else:
        num = num - 1
    steps -= 1
print(num)
