def equilibriumPoint(arr, n):
    if n == 1:
        return 1
    
    total = sum(arr)
    currSum = 0

    for i in range(n):
        total -= arr[i]
        if total == currSum:
            return i + 1
        currSum += arr[i]
        
    return -1


# I've ABSOLUTELY NO IDEA why the below code is failing
def equilibriumPoint(arr, n):
    if n == 1:
        return arr[0]

    hashmap = {}
    total = sum(arr)
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        diff = total - curr_sum
        if diff in hashmap:
            return i + 1
        hashmap[curr_sum] = i

    return -1
