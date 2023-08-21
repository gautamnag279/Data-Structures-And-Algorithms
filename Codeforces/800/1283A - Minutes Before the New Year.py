def solve(h, m):
    current = h*60 + m
    midnight = 1440
    print(abs(midnight - current))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, m = map(int, input().split())
        solve(h, m)
