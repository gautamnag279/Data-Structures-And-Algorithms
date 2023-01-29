# 140 ms, 5000 KB
def add(x):
    return sum([int(i) for i in str(x)])

def codeforces(n):
    if (add(n//1000) == add(n%1000)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        codeforces(int(input()))
        
# 93 ms, 3500 KB 
def codeforces(s):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    
    x = int(s[3])
    y = int(s[4])
    z = int(s[5])

    if (a+b+c == x+y+z):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    items = int(input())
    for i in range(items):
        codeforces(input())

