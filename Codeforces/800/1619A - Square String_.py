def isSquare(str):
    if (str[:len(str)//2] == str[len(str)//2:]):
        print("YES")
    else:
        print("NO")

n = int(input())
for i in range(n):
    isSquare(input())
