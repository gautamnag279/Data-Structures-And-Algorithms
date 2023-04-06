def evenArray(size, arr):
    oddIndexCount = 0
    evenIndexCount = 0
    for i in range(size):
        if (i % 2 != arr[i] % 2):
            if (arr[i] % 2 == 1):
                oddIndexCount += 1
            else:
                evenIndexCount += 1
    if oddIndexCount != evenIndexCount:
        print(-1)
    else:
        print(evenIndexCount)


if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        size = int(input())
        arr = list(map(int, input().split()))
        evenArray(size, arr)
