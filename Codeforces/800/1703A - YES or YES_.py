# 108 ms, 3100 KB
def codeforces(s):
    if s.lower() == "yes":
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        codeforces(input())

# 92 ms, 3700 KB
def codeforces(s):
    if s in ["yes", "YES", "Yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        codeforces(input())
