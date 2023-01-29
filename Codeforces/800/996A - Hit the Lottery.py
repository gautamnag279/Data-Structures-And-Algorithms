amount = int(input())
ans = 0
denominations = [100, 20, 10, 5, 1]
for i in range(5):
    ans += amount//denominations[i]
    amount %= denominations[i]
print(ans)
