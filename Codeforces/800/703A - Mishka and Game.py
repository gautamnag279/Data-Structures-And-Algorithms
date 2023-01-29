# 62 ms, 0 KB
if __name__ == "__main__":
    rounds = int(input())
    cMishka = 0
    cChris = 0
    for i in range(rounds):
        a, b = map(int, input().split(" "))
        if (a>b):
            cMishka += 1
        if (b>a):
            cChris += 1
    if cMishka > cChris:
        print("Mishka")
    elif cMishka < cChris:
        print("Chris")
    else:
        print("Friendship is magic!^^")
