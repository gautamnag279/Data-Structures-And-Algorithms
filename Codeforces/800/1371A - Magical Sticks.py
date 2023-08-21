def solve(n):
    pairs = n//2
    if n%2 == 1:
        pairs += 1
    print(pairs)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve(int(input()))
