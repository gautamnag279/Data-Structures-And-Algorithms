# 124 ms, 6000 KB
def guessString(s):
    for i in range(0, len(s), 2):
        print(s[i], end = "")
    print(s[len(s)-1])

n = int(input())
for i in range(n):
    guessString(input())
    
    
    
# 93 ms, 3500 KB
def guessString(s):
    newS = ""
    for i in range(0, len(s), 2):
        newS += s[i]
    print(newS+s[len(s) - 1])

n = int(input())
for i in range(n):
    guessString(input())
