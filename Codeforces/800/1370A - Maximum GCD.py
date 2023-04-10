from math import floor

def maxDivisor(n):
    print(floor(n/2))

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        maxDivisor(int(input()))