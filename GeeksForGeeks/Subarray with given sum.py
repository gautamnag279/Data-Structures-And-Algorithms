# Approach 1/2
def subArraySum(arr, n, s):
    left, right, currSum = 0, 0, 0
    for i in range(n):
        currSum += arr[i]
        if (currSum > s):
            while currSum > s:
                currSum -= arr[left]
                left += 1
        if (currSum == s):
            right = i
            break
    if (currSum != s):
        return [-1]
    else:
        return left+1, right+1

# Approach 2/2
def subArraySum(arr, n, s):
    hashMap = {}
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        if currSum == s:
            return [1, i+1]
        diff = currSum - s
        if diff in hashMap:
            return [hashMap[diff]+2, i+1]
        hashMap[currSum] = i
    return [-1]
