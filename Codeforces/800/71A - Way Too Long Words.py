n = int(input())
for i in range(0, n):
    word = input()
    if len(word) > 10:
        ans = str(word[0] + str(len(word) - 2) + word[-1])
        print(ans)
    else:
        print(word)
