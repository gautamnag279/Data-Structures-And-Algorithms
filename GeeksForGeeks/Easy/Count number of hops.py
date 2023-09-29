def countWays(n):
    ways = [0] * (n + 1)

    ways[0] = 1

    for i in range(1, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[n]
