def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n, m = map(int, input().split())
    nextPrime = n + 1
    while not isPrime(nextPrime):
        nextPrime += 1
    if nextPrime == m:
        print("YES")
    else:
        print("NO")
