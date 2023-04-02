def isPossible(size):
    if size % 4 != 0:
        print("NO")
    else:
        print("YES")
        sumEven = 0
        sumOdd = 0
        for i in range(2, size + 1, 2):
            print(i, end=" ")
            sumEven += i
        for j in range(1, size - 2, 2):
            print(j, end=" ")
            sumOdd += j
        print(sumEven - sumOdd)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        isPossible(int(input()))
