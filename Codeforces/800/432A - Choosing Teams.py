#62 ms, 1700 KB
def countOfMax(items, highest, arr):
    count = 0
    for i in arr:
        if (i + highest) <= 5:
            count += 1
    print(count//3)

if __name__ == "__main__":
    items, highest = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    countOfMax(items, highest, arr)
