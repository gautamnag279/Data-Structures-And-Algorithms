k, l, m, n, d = [int(input()) for i in range(5)]
count = d
if(k == 1 or l == 1 or m == 1 or n == 1):
    print(d)
else:
    for i in range(d+1):
        if(i%k != 0 and i%l != 0 and i%m != 0 and i%n != 0):
            count -= 1
    print(count)

# THIS TOO ME AN EMBARASSINGLY LONG AMOUNT OF TIME TO SOLVE 😔
