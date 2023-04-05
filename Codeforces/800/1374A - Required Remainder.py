def maxPossible(x, y, n):
    k = n - (n % x) + y
    if k > n:
        k -= x
    print(k)


if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        x, y, n = list(map(int, input().split()))
        maxPossible(x, y, n)

'''
Here's an easier way to approach the problem:

- Start with the largest possible value of k, which is n.
- Subtract the remainder of n divided by x from k. This gives us the largest number less than or equal to n that is divisible by x.
- Add y to k to get the largest number less than or equal to n that leaves a remainder of y when divided by x.
- If the result is greater than n, subtract x from k to get the largest number less than or equal to n that leaves a remainder of y when divided by x.
'''