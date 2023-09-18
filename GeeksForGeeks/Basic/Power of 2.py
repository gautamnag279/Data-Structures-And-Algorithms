def isPowerofTwo(n):
    if n > 0 and (n & (n - 1)) == 0:
        return 1
