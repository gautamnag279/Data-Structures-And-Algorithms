def minIncrement(arr):
    print(max(arr) - min(arr))

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        size = int(input())
        arr = list(map(int, input().split()))
        minIncrement(arr)
