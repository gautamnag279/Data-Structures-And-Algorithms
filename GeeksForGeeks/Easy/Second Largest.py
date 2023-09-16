def print2largest(arr, n):
    arr.sort()
    ans = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] != arr[i-1]:
            ans = arr[i-1]
            break
    if ans == 0:
        return -1
    return ans