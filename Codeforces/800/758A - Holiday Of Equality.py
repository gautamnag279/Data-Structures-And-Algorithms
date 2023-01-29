# 62 ms, 0 KB
def minIncentive(arr):
    richest = max(arr)
    count = 0
    for i in arr:
        count += (richest - i)
    print(count)

if __name__ == "__main__":
    items = int(input())
    minIncentive(list(map(int, input().split(" "))))

