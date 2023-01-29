# 46 ms, 1300 KB
def isPrime(x):
    bool = False
    for i in range(2, x):
        if x%i == 0:
            bool = True
            break
    return bool

if __name__ == "__main__":
    n = int(input())
    n1 = 0
    for i in range(4, n):
        if (isPrime(i) == True and isPrime(n-i)==True):
            print(i, n-i)
            break
