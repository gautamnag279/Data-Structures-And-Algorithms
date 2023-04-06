def isSum(arr):
    arr.sort()
    if arr[0] + arr[1] == arr[2]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        isSum(arr)