def getFirstSetBit(n):
    if n == 0:
        return 0
    return (n & -n).bit_length()