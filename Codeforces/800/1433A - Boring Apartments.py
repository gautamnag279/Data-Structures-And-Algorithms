# 46 ms, 0 KB
def boringSum(n):
    lst = [1, 2, 3, 4]

    add1 = sum(lst)*(int(n[0])-1)
    add2 = sum(lst[:len(n)])

    print(add1 + add2)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        boringSum(input())
