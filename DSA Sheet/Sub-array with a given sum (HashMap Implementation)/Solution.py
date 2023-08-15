def subArraySum(arr, n, s):
    hashmap = {}
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        
        if (currSum == s):
            return [1, i+1]  # 1-based indexing
        
        diff = currSum - s
        
        if diff in hashmap:
            return [hashmap[diff] + 2, i+1]  # 1-based indexing
        
        hashmap[currSum] = i


if __name__ == "__main__":
    print(subArraySum([1, 2, 3, 5, 7], 5, 12))
