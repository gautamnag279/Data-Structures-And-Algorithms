def convertToWave(n, a):
    for i in range(0, n-1, 2):
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
    return a