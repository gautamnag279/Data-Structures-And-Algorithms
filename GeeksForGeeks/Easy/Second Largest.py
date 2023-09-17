# Approach 1/2 - Intuitive
def print2largest(arr, n):
    arr.sort()
    ans = 0

    for i in range(n-1, -1, -1):
        if arr[i] != arr[i-1]:
            ans = arr[i-1]
            break

    if ans == 0:
        return -1
    
    return ans


# Approach 2/2
def print2largest(arr, n):
    if n < 2:
        return arr[0]
    
    largest = float('inf')
    second_largest = float('inf')

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    if second_largest == float('-inf'):
        return -1
    
    return second_largest
