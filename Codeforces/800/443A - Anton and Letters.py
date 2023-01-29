n = input()
size = n[1:len(n)-1].replace("," , "").replace(" ", "")

print(len(set(size)))
