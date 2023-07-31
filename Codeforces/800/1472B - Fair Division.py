def fairDivision(arr):
    alice = 0
    bob = 0
    arr.sort(reverse=True)
    for i in arr:
        if alice <= bob:
            alice += i
        else:
            bob += i
    if alice == bob:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        size = int(input())
        arr = list(map(int, input().split()))
        fairDivision(arr)
