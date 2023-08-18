def solve(s):
    if s in set('codeforces'):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        solve((input()))