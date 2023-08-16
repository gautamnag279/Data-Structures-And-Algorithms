def subArraySum(arr, n, s):
    hashmap = {}
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        if currSum == s:
            return [1, i + 1]  # 1-based indexing
        diff = currSum - s
        if diff in hashmap:
            return [hashmap[diff] + 2, i + 1]  # 1-based indexing
        hashmap[currSum] = i