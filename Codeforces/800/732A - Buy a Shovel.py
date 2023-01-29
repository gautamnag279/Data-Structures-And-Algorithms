def canBuy(priceOfOne, change):
    total = 0
    for i in range(1, 1000):
        total = priceOfOne*i
        if (total%10 == 0 or total%10 == change):
            print(i)
            break
        else:
            continue

priceOfOne, change = map(int, input().split(" "))
canBuy(priceOfOne, change)
