def printFibb(n):
    if n == 1:
        return [1]

    first = 1
    second = 1
    lst = [first, second]
    next = 0

    for i in range(n-2):
        next = first + second
        first = second
        second = next
        lst.append(second)

    return lst
