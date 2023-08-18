def solve(arr):
    mFirst = max(arr[0], arr[1])
    mSecond = max(arr[2], arr[3])
    if (mFirst < min(arr[2], arr[3])) or (mSecond < min(arr[0], arr[1])):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        solve(arr)
