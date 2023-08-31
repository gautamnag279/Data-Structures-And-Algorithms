def maxSubArraySum(arr, n):
    maxSum = float('-inf')
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        if (currSum < 0):
            currSum = 0
    return maxSum
