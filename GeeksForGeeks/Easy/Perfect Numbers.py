import math


def isPerfectNumber(N):
    if (N <= 1):
        return 0
    sum = 1
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            sum += (i + N//i)
    return int(sum == N)
