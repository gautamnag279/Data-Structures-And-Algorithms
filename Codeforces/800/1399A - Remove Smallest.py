def function(arr, size):
    isPossible = True

    arr.sort()
    for i in range(1, size):
        diff = abs(arr[i] - arr[i - 1])
        if diff > 1:
            isPossible = False
            break
            
    if isPossible:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        size = int(input())
        arr = list(map(int, input().split()))
        print(function(arr, size))

