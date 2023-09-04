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


print(leaders([16, 17, 4, 3, 5, 2], 6))
