k, n, w = map(int, input().split())
total = [k + k*i for i in range(0, w)]
if (n >= sum(total)):
    print(0)
else:
    print(sum(total) - n)
