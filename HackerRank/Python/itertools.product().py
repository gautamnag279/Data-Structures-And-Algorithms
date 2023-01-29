import itertools

row1 = map(int, input().split())
row2 = map(int, input().split())

#Note that there is an '*' before the function. This is needed otherwise the output will only be a map of the area the answer is stored
print(*itertools.product(row1, row2))
