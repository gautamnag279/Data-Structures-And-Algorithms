def solve(arr):
    arr.sort()
    print(arr[1])




if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        solve(arr)