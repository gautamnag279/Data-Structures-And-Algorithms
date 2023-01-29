num = int(input())
lst = []
for i in range(num + 1, 9014):
    if(len(set(str(i))) == len(str(num))):
        lst.append(i)
print(lst[0])
