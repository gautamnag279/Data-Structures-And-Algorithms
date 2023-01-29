import itertools

word, length = input().split(" ")
pairs = list(itertools.permutations(word, int(length)))
pairs.sort()

for i in pairs:
    print("".join(i))
