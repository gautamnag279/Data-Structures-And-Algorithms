def missingNumber(array, n):
    return int(n*(n+1)/2) - sum(array)
