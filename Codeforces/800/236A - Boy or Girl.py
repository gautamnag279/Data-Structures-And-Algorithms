x = input()
hashmap = []
for i in range(len(x)):
    if x[i] not in hashmap:
        hashmap.append(x[i])
if(len(hashmap) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
