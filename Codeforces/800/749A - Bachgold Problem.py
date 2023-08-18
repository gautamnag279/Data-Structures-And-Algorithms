def solve(n):
    if n % 2 == 1:
        n //= 2
        n -= 1
        print(n + 1)
        print(3, end=" ")
    else:
        n //= 2
        print(n)
    for _ in range(n):
        print(2, end=" ")
    print()


if __name__ == "__main__":
    n = int(input())
    solve(n)
