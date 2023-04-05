def maxPossible(x, y, n):
    k = n - (n % x) + y
    if k > n:
        k -= x
    print(k)


if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        x, y, n = list(map(int, input().split()))
        maxPossible(x, y, n)