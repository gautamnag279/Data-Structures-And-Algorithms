# 124 ms, 0 KB
def codeforces(s):
    length = len(s)
    p = ""
    i = 0
    while i < length:
        if (s[i] == "."):
            p+= '0'
        if (s[i] == "-" and s[i+1] == "."):
            p+= '1'
            i+=1
        if (s[i] == "-" and s[i+1] == "-"):
            p+='2'
            i+=1
        i+=1
    print(p)

if __name__ == "__main__":
    codeforces(input())
