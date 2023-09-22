def find(a, n, x):
    first = 0
    last = 0
    for i in range(n):
        if a[i] == x:
            first = i
            break
    for j in range(first, n):
        if a[j] > last and a[j] == x:
            last = j
    if first == 0 and last == 0:
        return -1, -1
    return first, last
