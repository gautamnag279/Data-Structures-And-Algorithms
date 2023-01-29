lst = [int(i) for i in input().split(" ")]
slst = set(lst)
print(abs(len(slst) - len(lst)))
