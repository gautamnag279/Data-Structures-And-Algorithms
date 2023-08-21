def solve(a, b, c):
    if (a + b == c):
        print("+")
    else:
        print("-")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        solve(a, b, c)
