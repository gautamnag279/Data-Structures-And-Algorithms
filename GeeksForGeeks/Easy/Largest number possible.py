def findLargest(N, S):
    if (N == 1 and S == 0):
        return 0
    if (S > 9*N or S == 0):
        return -1
    digits = [0 for _ in range(N)]
    for i in range(N):
        while S != 0 and digits[i] != 9:
            digits[i] += 1
            S -= 1
    return "".join(map(str, digits))
