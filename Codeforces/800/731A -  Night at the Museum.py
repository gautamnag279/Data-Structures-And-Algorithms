def solve(s):
    start = 'a'
    sum = 0
    for i in range(len(s)):
        clockwise = abs(ord(s[i]) - ord(start))
        antiClockwise = 26 - clockwise
        sum += min(clockwise, antiClockwise)
        start = s[i]
    print(sum)


if __name__ == "__main__":
    solve(input())
