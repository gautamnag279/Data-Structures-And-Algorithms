def solve(a, b, n, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        if i < k and b[i] > a[i]:
            a[i] = b[i]
    total_sum = sum(a)
    print(total_sum)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split())) 
        solve(a, b, n, k)
