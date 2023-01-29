def isEven(i):
    return i % 2 == 0


n = int(input())
ans = ""
for i in range(1, n+1):
    if isEven(i):
        ans += "I love that "
    else:
        ans += "I hate that "

print(ans[:len(ans) - 5] + "it")
