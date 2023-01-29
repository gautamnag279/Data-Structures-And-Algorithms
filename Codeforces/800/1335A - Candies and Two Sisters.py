def ways(n):
    midPoint = 0
    if(n % 2 == 0):
        midPoint = (n//2) - 1
    else:
        midPoint = (n-1)//2

    print(midPoint)


x = int(input())
for i in range(x):
    n = int(input())
    ways(n)
