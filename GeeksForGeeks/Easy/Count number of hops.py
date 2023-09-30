# Approach 1/2 - Intuitive
def countWays(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    a, b, c, ans = 1, 2, 4, 0
    for i in range(4, n+1):
        ans = (a+b+c) % 1000000007
        a = b
        b = c
        c = ans
    return ans


# Approach 2/2 - Dynamic Programming
def countWays(n):
    ways = [0] * (n + 1)

    ways[0] = 1

    for i in range(1, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[n]
