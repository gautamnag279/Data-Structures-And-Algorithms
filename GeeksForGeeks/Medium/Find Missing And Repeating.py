def findTwoElement(self, arr, n):
    l = []

    arr.sort()

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            l.append(arr[i])

    missing = (n*(n+1))//2 - (sum(arr) - l[0])
    l.append(missing)
    
    return l
