items = int(input())
shoes = list(map(int, input().split()))

count = 0
for i in set(shoes):
    elem = shoes.count(i)//2
    count = count + elem
print(count)
    
