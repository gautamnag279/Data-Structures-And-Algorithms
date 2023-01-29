# 108 ms, 5740 KB
def fairPlay(size, arr):
    arr2  =[]
    for i in range(len(arr)):
        if(arr[i] not in arr2):
            arr2.append(arr[i])
    print(*arr2)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        size = int(input())
        arr = list(map(int, input().split(" ")))
        fairPlay(size, arr)

