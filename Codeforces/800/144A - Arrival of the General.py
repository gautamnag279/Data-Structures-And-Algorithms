n = int(input())
arr = [int(i) for i in input().split(" ")]

maxValue = 0
minValue = 1000
iMax = 0
iMin = 0

for i in range(0, n):
    if(arr[i] > maxValue):
        iMax = i
        maxValue = arr[i]
    if(arr[i] <= minValue):
        iMin = i
        minValue = arr[i]

if(iMax > iMin):
    swaps = (iMax - 1) + (n - iMin) - 1
else:
    swaps = (iMax - 1) + (n - iMin)

print(swaps)
