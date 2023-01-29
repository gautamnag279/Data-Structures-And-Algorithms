# 234 ms, 8864 KB
def areAhead(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            count+= 1
    print(count)

if __name__ == "__main__":
    participants = int(input())
    for i in range(participants):
        areAhead(list(map(int, input().split(" "))))

