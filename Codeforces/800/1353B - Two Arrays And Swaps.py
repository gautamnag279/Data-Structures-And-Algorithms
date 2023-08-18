def solve(a, b, n, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        for j in range(n):
            if b[j] > a[j]:
                a[j], b[j] = b[j], a[j]
                break
    total_sum = sum(a)
    print(total_sum)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())  # 5,3
        a = list(map(int, input().split()))  # [1,2,3,4,5]
        b = list(map(int, input().split()))  # [10,9,10,10,9]
        solve(a, b, n, k)
