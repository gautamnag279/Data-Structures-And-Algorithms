def minDistance(houses):
    houses.sort()
    median = houses[1]

    for i in range(3):
        add = 0
        add += houses[2] - median
        add += median - houses[0]
    print(add)

friends = list(map(int, input().split(" ")))
minDistance(friends)
