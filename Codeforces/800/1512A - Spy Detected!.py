# 77 ms, 1600 KB
def oddOneOut(size, arr):
    uniques = set(arr)
    for i in uniques:
        if arr.count(i) == 1:
            print(arr.index(i) + 1)
            break

if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        arrSize = int(input())
        arr = list(map(int, input().split(" ")))
        oddOneOut(arrSize, arr)
