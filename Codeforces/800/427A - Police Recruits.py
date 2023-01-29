n = int(input())
arr = [int(i) for i in input().split(" ")]

police = 0
crime = 0

for i in range(n):
    if(arr[i] == -1):
        if(police > 0):
            police -= 1
        else:
            crime += 1
    else:
        police += arr[i]

print(crime)
