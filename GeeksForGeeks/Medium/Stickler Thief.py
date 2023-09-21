def FindMaxSum(a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
    
        prevSum = a[0]
        currSum = max(a[0], a[1])
    
        for i in range(2, n):
            newSum = max(currSum, prevSum + a[i])
            prevSum = currSum
            currSum = newSum
    
        return currSum
