#all you need to do is delete the smallest element from list n then print the lenth of list

n = int(input())
arr = [int(i) for i in input().split()][:n]

print(len(arr))
while len(arr) > 0:
    arr = [i for i in arr if i != min(arr)]
    if len(arr) == 0:
        break
    print(len(arr))
