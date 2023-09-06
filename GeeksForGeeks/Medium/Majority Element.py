def majorityElement(A, N):
    count = 0
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            count += 1
        if count == N//2:
            return A[i]
        if A[i] != A[i+1]:
            count = 0
    return -1

a = [1,2]
n = len(a)
print(majorityElement(a, n))