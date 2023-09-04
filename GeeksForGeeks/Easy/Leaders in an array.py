def leaders(A, N):
    A = A[::-1]
    leaders = []
    max = 0
    for i in A:
        if i >= max:
            max = i
            leaders.append(max)
    leaders.reverse()
    return leaders
