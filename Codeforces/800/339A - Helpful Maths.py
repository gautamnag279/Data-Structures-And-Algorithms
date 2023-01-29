x = [int(i) for i in input().replace("+" , "")]
x.sort()
print('+'.join(str(i) for i in x))
