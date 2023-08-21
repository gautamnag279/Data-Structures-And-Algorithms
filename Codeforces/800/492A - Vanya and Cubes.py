def solve(n):
    i = 0
    element = 0
    sum = 0
    while sum <= n:
        i += 1
        element += i
        if (sum > n):
            break
        sum += element
    print(i-1)


if __name__ == "__main__":
    solve(int(input()))
