h = list(map(int , input().strip().split()))
word = list(input().strip())

lst = []
rank = []

for i in word:
    elem = ord(i) - ord('a')
    lst.append(elem)

for a in lst:
    for b in range(0 ,len(h)):
        if a == b:
            rank.append(h[b])
            
print(max(rank)*len(rank))
