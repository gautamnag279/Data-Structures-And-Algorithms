n = int(input())
parts = list(int(i)/100 for i in input().split(" "))
print((sum(parts)/n)*100)
