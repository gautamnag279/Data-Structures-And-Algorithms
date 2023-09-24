def getMinDiff(arr, n, k):
    arr.sort()
    
    diff = arr[n-1] - arr[0]
    
    tallest = arr[n-1] - k
    shortest = arr[0] + k
    
    curr_tallest = 0
    curr_shortest = 0
    
    for i in range(n-1):
        curr_tallest = max(arr[i]+k, tallest)
        curr_shortest = min(arr[i+1]-k, shortest)

        if curr_shortest < 0:
            continue
        else:
            diff = min(diff, curr_tallest - curr_shortest)
    
    return diff