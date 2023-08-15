def maxSubArraySum(arr, N):
    # Your code here
    maxSum = float('-inf')
    currentSum = 0
    for i in range(N):
        currentSum += arr[i]
        maxSum = max(maxSum, currentSum)
        if currentSum < 0:
            currentSum = 0
    return maxSum


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(maxSubArraySum(arr, n))
